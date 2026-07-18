from machine import Pin
import time

armed_led = Pin("LED", Pin.OUT)
disarmed_led = Pin(16, Pin.OUT)  
button = Pin(14, Pin.IN, Pin.PULL_DOWN)

system_armed = False
last_press_time = 0

def toggle_system():
    global system_armed
    system_armed = not system_armed
    print(f"System is now {'ARMED' if system_armed else 'DISARMED'}")

time.sleep(0.5)

while True:
    if button.value() == 1 and (time.ticks_ms() - last_press_time) > 300:
        toggle_system()
        last_press_time = time.ticks_ms()
        
    if system_armed:
        armed_led.value(1)
        disarmed_led.value(0)
    else:
        armed_led.value(0)
        disarmed_led.value(1)
        
    time.sleep(0.05)