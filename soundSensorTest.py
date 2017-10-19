#!/usr/bin/python3
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges. You can achieve this by using 'sudo' to run your script")
import time

# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
PIN = 14

# set up GPIO input channel
GPIO.setup(PIN, GPIO.IN)

def measure_sound():
    sound = GPIO.input(14)
    return sound

while True:
    sound = measure_sound()
    print(sound)
    time.sleep(1)