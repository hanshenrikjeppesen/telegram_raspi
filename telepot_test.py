#!/usr/bin/python3

import sys
import time
import random
import datetime
import telepot
import RPi.GPIO as GPIO

#LED
def on(pin):
        GPIO.output(pin,GPIO.HIGH)
        return
def off(pin):
        GPIO.output(pin,GPIO.LOW)
        return

# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BCM)

# set up GPIO output channel
GPIO.setup(17, GPIO.OUT)

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print ('Got command: {}'.format(command))

    if command == 'on':
       bot.sendMessage(chat_id, on(17))
    elif command =='off':
       bot.sendMessage(chat_id, off(17))

bot = telepot.Bot('479647911:AAF3lzp-5g9G-VBkU31duAMwWsTVHnmUzBA')
bot.message_loop(handle)
print ('I am listening...')

while 1:
     time.sleep(10)
