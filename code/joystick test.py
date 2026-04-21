from machine import ADC, Pin
import time

joy = ADC(Pin(35))
joy.atten(ADC.ATTN_11DB)

while True:
    print(joy.read())
    time.sleep(0.2)