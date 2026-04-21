from machine import Pin, SPI, ADC
import max7219
import time
import random

# ---------- DISPLAY ----------
spi = SPI(1, baudrate=80000, polarity=0, phase=0,
          sck=Pin(18), mosi=Pin(23))

cs1 = Pin(5, Pin.OUT)
cs2 = Pin(15, Pin.OUT)

display1 = max7219.Matrix8x8(spi, cs1, 4)
display2 = max7219.Matrix8x8(spi, cs2, 4)

WIDTH = 32
HEIGHT = 8

# ---------- MIC ----------
mic = ADC(Pin(34))
mic.atten(ADC.ATTN_11DB)

baseline = 1900
prev_value = 0

# ---------- JOYSTICK ----------
joy = ADC(Pin(35))
joy.atten(ADC.ATTN_11DB)

mode = 2  # 1 = bass, 2 = full, 3 = treble
prev_region = 2  # for flick detection

# ---------- ARRAYS ----------
current = [0]*WIDTH
target = [0]*WIDTH

NOISE_THRESHOLD = 8

# ---------- FILTER MEMORY ----------
low = 0
high = 0

while True:

    display1.fill(0)
    display2.fill(0)

    # ---------- JOYSTICK READ ----------
    joy_val = joy.read()

    # classify joystick position
    if joy_val < 1200:
        region = 1   # UP
    elif joy_val > 2800:
        region = 3   # DOWN
    else:
        region = 2   # CENTER

    # ---------- FLICK LOGIC (EDGE DETECTION) ----------
    if region != prev_region:

        # CENTER → UP = MODE UP
        if prev_region == 2 and region == 1:
            mode += 1

        # CENTER → DOWN = MODE DOWN
        elif prev_region == 2 and region == 3:
            mode -= 1

        # clamp mode
        if mode < 1:
            mode = 1
        if mode > 3:
            mode = 3

        # DEBUG OUTPUT
        if mode == 1:
            print("🎛 MODE: BASS")
        elif mode == 2:
            print("🎛 MODE: FULL")
        else:
            print("🎛 MODE: TREBLE")

    prev_region = region

    # ---------- MIC READ ----------
    value = mic.read()
    baseline = (baseline * 0.9) + (value * 0.1)

    amplitude = abs(value - baseline)
    delta = abs(value - prev_value)
    prev_value = value

    if amplitude < NOISE_THRESHOLD:
        amplitude = 0
        delta = 0

    # ---------- FILTERS ----------
    low = (low * 0.95) + (amplitude * 0.05)
    full = (amplitude * 0.6) + (low * 0.4)
    high = (high * 0.3) + (delta * 0.7)

    # ---------- MODE SELECTION ----------
    if mode == 1:
        band_val = low
    elif mode == 2:
        band_val = full
    else:
        band_val = high

    # ---------- VISUALIZER ----------
    for x in range(WIDTH):

        if amplitude == 0:
            target[x] = 0
        else:
            if mode == 2:
                variation = band_val + random.randint(-25, 25)
            else:
                variation = band_val + random.randint(-15, 15)

            height = int(variation / 10)

            if height < 0:
                height = 0
            if height > HEIGHT:
                height = HEIGHT

            target[x] = height

        # smooth movement
        if current[x] < target[x]:
            current[x] += 1
        elif current[x] > target[x]:
            current[x] -= 1

        if amplitude == 0:
            current[x] = max(0, current[x] - 1)

        h = current[x]

        # bottom → top display1
        for y in range(h):
            display1.pixel(x, 7 - y, 1)

        # top → bottom display2
        for y in range(h):
            display2.pixel(x, y, 1)

    display1.show()
    display2.show()

    time.sleep(0.05)