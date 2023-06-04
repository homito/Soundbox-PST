# 1.3" mono-colored oled display 128*64
# https://luma-oled.readthedocs.io/en/latest/

from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1325, ssd1331, sh1106

from pathlib import Path
from PIL import ImageFont, Image

import time
import os
import subprocess
import sys

metadata = {
    "State": "pending", #or "active" or "idle"
    "Title": "unknown",
    "Artist": "unknown",
    "Album": "unknown", #should not be displayed
    "Status": "stopped", #or "playing"
    "Position" : "0",
    "Duration": "0",
    "TrackNumber": "0", #should not be displayed
    "NumberOfTracks": "0", #should not be displayed
    "Volume": "0",
    "Device": "unknown"
}

State = 0 # 0 = not paired, 1 = paired

serial = i2c(port=1, address=0x3C)
device = sh1106(serial, rotate=0)

width = 128
height = 64

file = "/usr/src/app/logs.txt"
file_data = "/shared/logs/data.log"

def specialSort(str):
    # this functions takes a string as an input and returns another string without any special characters if there were any
    for c in str:
        if not (c.isascii()):
            str = str.replace(c, "?")
    return str
    

def getMetadata():
    txt = open(file, "r")
    lines = txt.readlines()
    for line in lines:
        key = line[:line.find(":")-1]
        value = specialSort(line[line.find(":")+2:-1])
        metadata[key] = value
    txt.close()

def displayMetadata():
    now = time.strftime("%H:%M")
    draw.text((0,0), now, fill="white")

    if metadata["Title"] == "unknown" and metadata["Artist"] == "unknown":
        w, h = draw.textsize("Waiting for music...")
        left = (width - w) / 2
        top = (height - h) / 2
        draw.text((left, top), "Waiting for music...", fill="white")
        return
    
    w, h = draw.textsize(metadata["Title"])
    left = (width - w) / 2
    top = (height - h) / 2
    draw.text((left, top), metadata["Title"], fill="white")

    w, h = draw.textsize(metadata["Artist"])
    left = (width - w) / 2
    top = ((height - h) / 2) + 10
    draw.text((left, top), metadata["Artist"], fill="white")


    #draw.text((128/2 - len(metadata["Title"]*3),0), metadata["Title"], fill="white")
    #draw.text((128/2 - len(metadata["Artist"]*3),10), metadata["Artist"], fill="white")

def displayBootScreen():
    w, h = draw.textsize('SOUNDBOX')
    left = (width - w) / 2
    top = (height - h) / 2
    draw.text((left, top), 'SOUNDBOX', fill="white")

def displayPairingScreen():
    global State
    w, h = draw.textsize('Waiting for pairing.')
    left = (width - w) / 2
    top = (height - h) / 2

    txt = open(file_data, "r")
    lines = txt.readlines()
    for line in lines:
        if (line.find("State: 1") != -1):
            State = 1
            break
    draw.text((left, top), 'Waiting for pairing.', fill="white")

i = 0
while(True):
    with canvas(device) as draw:
        try:
            if os.path.exists(file_data) == False:
                displayBootScreen()
            elif State == 0:
                displayPairingScreen()
            elif State == 1:
                getMetadata()
                displayMetadata()
        except:
            try:
                displayBootScreen()
                print("ERROR: 1 - problem on display")
            except:
                print("ERROR: 2 - final problem on display")

    i += 1

#known issues: special characters break everything