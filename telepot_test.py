#!/usr/bin/python3

import sys
import time
import random
import datetime
import telepot
import RPi.GPIO as GPIO

#LED
def on(pin):
    GPIO.output(pin, GPIO.HIGH)
    return
def off(pin):
    GPIO.output(pin,GPIO.LOW)
    return

# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
PIN = 23

# set up GPIO output channel
GPIO.setup(PIN, GPIO.OUT)

bot = telepot.Bot('479647911:AAF3lzp-5g9G-VBkU31duAMwWsTVHnmUzBA')

def reciveMsg():
    try:
        incomming = bot.getUpdates()
    except Exception:
        sys.exc_clear()

    numOfIncomming = len(incomming)
    print(numOfIncomming)

while True:
    reciveMsg()
    time.sleep(1000)
    '''
    if command == 'On':
        GPIO.output(PIN, GPIO.HIGH)
    if command =='Off':
        GPIO.output(PIN, GPIO.LOW)
'''