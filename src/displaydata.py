# 1.3" mono-colored oled display 128*64
# https://luma-oled.readthedocs.io/en/latest/

from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1325, ssd1331, sh1106

from pathlib import Path
from PIL import ImageFont, Image

import time
import os

metadata = {
    "State": "pending", #or "active" or "idle"
    "Title": "unknown",
    "Artist": "unknown",
    "Album": "unknown", #should not be displayed
    "Status": "stopped", #or "playing"
    "Position" : 0,
    "Duration": 0,
    "TrackNumber": 0, #should not be displayed
    "NumberOfTracks": 0, #should not be displayed
    "Volume": 0,
    "Device": "unknown"
}

serial = i2c(port=1, address=0x3C)
device = sh1106(serial, rotate=0)

width = 128
height = 64

file = "/usr/src/app/logs.txt"

def getMetadata():
    txt = open(file, "r")
    lines = txt.readlines()
    for line in lines:
        key = line[:line.find(":")-1]
        value = line[line.find(":")+2:-1]
        metadata[key] = value
    txt.close()

def displayMetadata():
    draw.text((128/2 - len(metadata["Title"]*3),0), metadata["Title"], fill="white")
    draw.text((128/2 - len(metadata["Artist"]*3),10), metadata["Artist"], fill="white")
    draw.text((0,50), metadata["Device"], fill="white")

def displayInitScreen():
    w, h = draw.textsize('SOUNDBOX')
    left = (width - w) / 2
    top = (height - h) / 2
    draw.text((left, top), 'SOUNDBOX', fill="white")

def roundDown(var):
    if round(var) != round(var-0.5):
        return round(var-0.5)
    return round(var)

def ConvertMS(miliseconds):
    # convert a time in miliseconds to one in hh:mm:ss format
    seconds = roundDown(miliseconds/1000)

    minutes = roundDown(seconds/60)
    seconds = seconds - minutes*60

    hours = roundDown(minutes/60)
    minutes = minutes - hours*60

    time = []
    if hours>0:
        time.append(str(hours)+':')
        if minutes<10:
            time.append(0)
    time.append(str(minutes)+':')
    if seconds<10:
        time.append('0')
    time.append(str(seconds))

    time = ''.join(time)
    return time

i = 0
while(i<1000):
    with canvas(device) as draw:
        if i<20:
            displayInitScreen()
        elif i<40:
            draw.text((0,0), "Loading...", fill="white")
        else:
            try:
                getMetadata()
                displayMetadata()
            except:
                print("Error")
    i += 1