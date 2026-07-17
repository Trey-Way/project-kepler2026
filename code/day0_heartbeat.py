from machine import Pin
import time

led = Pin("LED", Pin.OUT)

print("SYSTEM H E A R T B E A T ON!")

while True:
    led.toggle()
    time.sleep(0.5)