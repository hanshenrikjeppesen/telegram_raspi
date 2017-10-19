#!/usr/bin/python3
import RPi.GPIO as GPIO

# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
PIN = 14

# set up GPIO output channel
GPIO.setup(PIN, GPIO.IN)

def measure_sound():
  
