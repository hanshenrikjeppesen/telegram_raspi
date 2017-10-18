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

    if numOfIncomming > 1:
        msg = incomming[numOfIncomming - 1]
    else:
        msg = incomming[0]

    newMsg = msg.get('message')

    text = newMsg.get('text')

    return text

while True:
    command = reciveMsg().lower()
    if command == 'on':
        GPIO.output(PIN, GPIO.HIGH)
    elif command =='off':
        GPIO.output(PIN, GPIO.LOW)
    elif command == 'blink':
        for i in range(10):
            GPIO.output(PIN, GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(PIN, GPIO.LOW)
            time.sleep(0.1)
    time.sleep(2)
