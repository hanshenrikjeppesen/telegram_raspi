#!/usr/bin/python3

import sys
import time
import random
import datetime
import telepot
import RPi.GPIO as GPIO

#LED
def on(pin):
    GPIO.output(pin,GPIO.TRUE)
    return
def off(pin):
    GPIO.output(pin,GPIO.FALSE)
    return

# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BCM)

# set up GPIO output channel
GPIO.setup(14, GPIO.OUT)

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print ('Got command: {}'.format(command))

    if command == 'on':
        on(14)
    elif command =='off':
        off(14)

bot = telepot.Bot('479647911:AAF3lzp-5g9G-VBkU31duAMwWsTVHnmUzBA')
bot.message_loop(handle)
print ('I am listening...')

while 1:
     time.sleep(10)
