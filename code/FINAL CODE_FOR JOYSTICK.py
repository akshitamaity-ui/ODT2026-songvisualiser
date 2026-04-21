# ─────────────────────────────────────────────
#  SONIC VAULT — ESP32 Joystick Controller
#  Flash this with Thonny as main.py
# ─────────────────────────────────────────────

import machine
import time

# ── PIN SETUP ──────────────────────────────────
x_axis = machine.ADC(machine.Pin(35))
y_axis = machine.ADC(machine.Pin(34))
btn = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_UP)

x_axis.atten(machine.ADC.ATTN_11DB)
y_axis.atten(machine.ADC.ATTN_11DB)

# ── THRESHOLDS ─────────────────────────────────
LOW  = 1500    
HIGH = 2500   

# ── STATE ──────────────────────────────────────
last_cmd      = None   
btn_was_down  = False  

# ─────────────────────────────────────────────
def get_command():
    """
    Read joystick and return command. 
    Y-axis inverted as requested.
    """
    x = x_axis.read()
    y = y_axis.read()

    # SWAPPED: HIGH now returns UP, LOW now returns DOWN
    if y > HIGH:           
        return "UP"
    elif y < LOW:          
        return "DOWN"
    elif x > HIGH:         
        return "RIGHT"
    elif x < LOW:          
        return "LEFT"
    else:                  
        return None  

# ─────────────────────────────────────────────
def send(cmd):
    print(cmd)

# ─────────────────────────────────────────────
#  MAIN LOOP
# ─────────────────────────────────────────────
print("SONIC VAULT controller ready (Y-Axis Inverted).")

while True:
    cmd = get_command()

    if cmd and cmd != last_cmd:
        send(cmd)
        last_cmd = cmd
    elif not cmd:
        last_cmd = None

    btn_pressed = (btn.value() == 0)
    if btn_pressed and not btn_was_down:
        send("SELECT")

    btn_was_down = btn_pressed
    time.sleep(0.05)