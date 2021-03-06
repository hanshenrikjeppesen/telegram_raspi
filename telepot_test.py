#!/usr/bin/python3

import sys
import time
import os
import telepot
import RPi.GPIO as GPIO

#LED
def LEDon():
    GPIO.output(23, GPIO.HIGH)
    return
def LEDoff():
    GPIO.output(23,GPIO.LOW)
    return
def LEDblink():
    for i in range(10):
        GPIO.output(23, GPIO.HIGH)
        time.sleep(0.05)
        GPIO.output(23, GPIO.LOW)
        time.sleep(0.05)

# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
oldCommand = 'qwerty'

# set up GPIO output channel
GPIO.setup(23, GPIO.OUT)
GPIO.setup(14, GPIO.IN)

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
        pass

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

def measure_sound():
    sound = GPIO.input(14)
    return sound

while True:
    name, id, command = reciveMsg()
    temp = measure_temp()
    coffeeTime = measure_sound()
    if temp > 60:
        sys.exit()
    if command != oldCommand:
        if command == 'on':
            LEDon()
            oldCommand = command
        elif command =='off':
            LEDoff()
            oldCommand = command
        elif command == 'shotgun':
            LEDblink()
            oldCommand = command
        if command == 'temp':
            bot.sendMessage(id, 'Hey ' + name + ' Temp of CPU on Raspi is.: ' + str(temp) + 'C')
            oldCommand = command
        if command == 'coffee':
            if coffeeTime == 1:
                bot.sendMessage(id, 'Hey ' + name + ' sorry, someone is making coffe, call shotgun')
                oldCommand = command
            else:
                bot.sendMessage(id, 'Hey ' + name + " It's CoffeeTime!!!")
                oldCommand = command
    time.sleep(2)
