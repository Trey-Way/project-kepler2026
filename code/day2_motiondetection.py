from machine import Pin
import time

armed_led = Pin ("LED", Pin.OUT)
disarmed_led = Pin(16, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_DOWN)
pir = Pin(13, Pin.IN)

system_armed = False
last_press_time = 0

def toggle_system():
    global system_armed
    system_armed= not system_armed
    print(f"System is now {'ARMED' if system_armed else 'DISARMED'}")

print("PIR warming up...")
time.sleep(30)
print("Ready.")

while True:
    if button.value() == 1 and (time.ticks_ms() - last_press_time) > 300:
        toggle_system()
        last_press_time = time.ticks_ms()
    if system_armed and pir.value() == 1:
        print(" INTRUSION DETECTED!!!! Get ready.. or else ")
        for i in range(10):
            armed_led.value(1)
            disarmed_led.value(1)
            time.sleep(0.1)
            armed_led.value(0)
            disarmed_led.value(0)
            time.sleep(0.1)
        armed_led.value(1)
        disarmed_led.value(0)
        time.sleep(2)
    else:
        if system_armed:
            armed_led.value(1)
            disarmed_led.value(0)
        else:
            armed_led.value(0)
            disarmed_led.value(1)
    
    time.sleep(0.05)