#!/usr/bin/python3

import sys
import time
import random
import datetime
import telepot
import RPi.GPIO as GPIO

#LED
def on(pin):
    GPIO.output(pin, GPIO.TRUE)
    return
def off(pin):
    GPIO.output(pin,GPIO.FALSE)
    return

# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
PIN = 23

# set up GPIO output channel
GPIO.setup(PIN, GPIO.OUT)

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print ('Got command: {}'.format(command))
    return command
    if command == 'On':
        GPIO.output(PIN, GPIO.HIGH)
    if command =='Off':
        GPIO.output(PIN, GPIO.LOW)

bot = telepot.Bot('479647911:AAF3lzp-5g9G-VBkU31duAMwWsTVHnmUzBA')
bot.message_loop(handle)
print ('I am listening...')
while 1:
     time.sleep(10)
