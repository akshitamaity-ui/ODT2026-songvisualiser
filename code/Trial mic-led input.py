from machine import Pin, SPI, ADC
import max7219
import time
import random

# ---------- SPI + DISPLAY SETUP ----------
spi = SPI(1, baudrate=80000, polarity=0, phase=0,
          sck=Pin(18), mosi=Pin(23))

cs1 = Pin(5, Pin.OUT)    # Display 1
cs2 = Pin(15, Pin.OUT)   # Display 2

display1 = max7219.Matrix8x8(spi, cs1, 4)
display2 = max7219.Matrix8x8(spi, cs2, 4)

WIDTH = 32
HEIGHT = 8

# ---------- MIC SETUP ----------
mic = ADC(Pin(34))
mic.atten(ADC.ATTN_11DB)

baseline = 1900

# ---------- VISUAL DATA ----------
current = [0]*WIDTH
target = [0]*WIDTH

NOISE_THRESHOLD = 5  #  adjust if needed

# ---------- MAIN LOOP ----------
while True:

    display1.fill(0)
    display2.fill(0)

    # read mic
    value = mic.read()
    baseline = (baseline * 0.9) + (value * 0.1)
    amplitude = abs(value - baseline)

    # 🔹 noise gate (flat when silent)
    if amplitude < NOISE_THRESHOLD:
        amplitude = 0

    for x in range(WIDTH):

        # ---------- TARGET HEIGHT ----------
        if amplitude == 0:
            target[x] = 0
        else:
            variation = amplitude + random.randint(-20, 20)

            height = int(variation / 8)

            if height < 0:
                height = 0
            if height > HEIGHT:
                height = HEIGHT

            target[x] = height

        # ---------- SMOOTH MOVEMENT ----------
        if current[x] < target[x]:
            current[x] += 1
        elif current[x] > target[x]:
            current[x] -= 1

        # faster drop when silent
        if amplitude == 0:
            current[x] = max(0, current[x] - 1)

        h = current[x]

        # ---------- DRAW ----------
        # Display 1: bottom → top
        for y in range(h):
            display1.pixel(x, 7 - y, 1)

        # Display 2: top → bottom
        for y in range(h):
            display2.pixel(x, y, 1)

    # update both displays together
    display1.show()
    display2.show()

    time.sleep(0.06)