# ─────────────────────────────────────────────
#  SONIC VAULT — ESP32 Joystick Controller
#  Flash this with Thonny as main.py
#
#  Wiring:
#   Joystick VCC  → 3.3V
#   Joystick GND  → GND
#   Joystick VRX  → GPIO 34  (X-axis)
#   Joystick VRY  → GPIO 35  (Y-axis)
#   Joystick SW   → GPIO 13  (button)
# ─────────────────────────────────────────────

import machine
import time

# ── PIN SETUP ──────────────────────────────────
# ADC pins 34 and 35 are input-only on ESP32
# (safe choice for analog reads)
x_axis = machine.ADC(machine.Pin(35))
y_axis = machine.ADC(machine.Pin(34))

# Internal pull-up: button reads 0 when pressed
btn = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_UP)

# Set ADC range to full 0–4095 (12-bit)
x_axis.atten(machine.ADC.ATTN_11DB)
y_axis.atten(machine.ADC.ATTN_11DB)

# ── THRESHOLDS ─────────────────────────────────
# Center rests around 2048.
# Adjust LOW/HIGH if your joystick drifts.
LOW  = 1500    # below this = pushed UP or LEFT
HIGH = 2500   # above this = pushed DOWN or RIGHT

# ── STATE ──────────────────────────────────────
last_cmd      = None   # last command sent (prevents spamming)
btn_was_down  = False  # tracks button state between loops

# ─────────────────────────────────────────────
def get_command():
    """
    Read joystick and button, return a command string
    or None if the stick is in the neutral zone.

    Priority: Y-axis (DOWN/UP) → X-axis (RIGHT/LEFT) → Button
    """
    x = x_axis.read()
    y = y_axis.read()

    if   y < HIGH:           return "DOWN"
    elif y > LOW:          return "UP"
    elif x < HIGH:           return "RIGHT"
    elif x > LOW:          return "LEFT"
    else:                   return None   # neutral / centre

# ─────────────────────────────────────────────
def send(cmd):
    """Print the command over USB serial (what WebSerial reads)."""
    print(cmd)

# ─────────────────────────────────────────────
#  MAIN LOOP
# ─────────────────────────────────────────────
print("SONIC VAULT controller ready.")

while True:

    # ── JOYSTICK ────────────────────────────────
    cmd = get_command()

    if cmd and cmd != last_cmd:
        # Stick moved into a new direction — send once
        send(cmd)
        last_cmd = cmd
    elif not cmd:
        # Stick returned to centre — reset so next tilt sends again
        last_cmd = None

    # ── BUTTON ──────────────────────────────────
    btn_pressed = (btn.value() == 0)

    if btn_pressed and not btn_was_down:
        # Fresh press — send SELECT
        send("SELECT")

    btn_was_down = btn_pressed

    # ── LOOP RATE ───────────────────────────────
    # 50 ms = 20 checks/sec — responsive but not noisy
    time.sleep(0.05)
