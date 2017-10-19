#!/usr/bin/python3

import sys
import time
import os
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
oldCommand = 'qwerty'

# set up GPIO output channel
GPIO.setup(PIN, GPIO.OUT)

# with open('/home/pi/token.txt', 'r') as f:
  #  readToken = f.readline()

bot = telepot.Bot('454245258:AAF2v9Y9aOlF4bSgDfZ6xLOyea3VGWsF8hY')

def measure_temp():
    temp = os.popen("vcgencmd measure_temp").readline()
    temp = temp.replace("temp=", "")
    temp = int(temp[0:2])
    return temp

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
    text = newMsg.get('text').lower()

    p = newMsg.get('from')
    id = p.get('id')
    name = p.get('first_name')

    return [name, id, text]



while True:
    name, id, command = reciveMsg()
    print(name, id, command)
    temp = measure_temp()
    if temp > 60:
        sys.exit()
    if command != oldCommand:
        if command == 'on':
            GPIO.output(PIN, GPIO.HIGH)
            oldCommand = command
        elif command =='off':
            GPIO.output(PIN, GPIO.LOW)
            oldCommand = command
        elif command == 'blink':
            for i in range(10):
                GPIO.output(PIN, GPIO.HIGH)
                time.sleep(0.1)
                GPIO.output(PIN, GPIO.LOW)
                time.sleep(0.1)
                oldCommand = command
        if command == 'temp':
            bot.sendMessage(id, 'Hey ' + name + ' Temp of CPU on Raspi is.: ' + str(temp) + 'C')
            oldCommand = command
        if command == 'coffee':
            bot.sendMessage(id, 'Hey ' + name + ' we are not ready yet, but we are working hard, tune in soon')
            oldCommand = command
    time.sleep(2)
