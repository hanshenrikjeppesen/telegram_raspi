#!/usr/bin/python3
import sys
import time
import os
import telepot
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges. You can achieve this by using 'sudo' to run your script")


# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
PIN = 14
oldCommand = 'qwerty'


# set up GPIO input channel
GPIO.setup(PIN, GPIO.IN)
bot = telepot.Bot('479647911:AAF3lzp-5g9G-VBkU31duAMwWsTVHnmUzBA')


def measure_temp():
    temp = os.popen("vcgencmd measure_temp").readline()
    temp = temp.replace("temp=", "")
    temp = int(temp[0:2])
    return temp

def measure_sound():
    sound = GPIO.input(14)
    return sound

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
    temp = measure_temp()
    if temp > 60:
        sys.exit()
    if command != oldCommand:
        if command == 'temp':
            bot.sendMessage(id, 'Hey ' + name + ' Temp of CPU on Raspi is.: ' + str(temp) + 'C')
            oldCommand = command
    if command == 'coffee':
        sound = measure_sound()
        if sound == 1:
            bot.sendMessage(id, 'Hey ' + name + 'There is one who makes coffee')
            oldCommand = command
        else:
            bot.sendMessage(id, 'Hey ' + name + 'the coffee machine is free')
            oldCommand = command
    time.sleep(1)

