# 1.3" mono-colored oled display 128*64
# https://luma-oled.readthedocs.io/en/latest/

from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1325, ssd1331, sh1106

import time
import os

metadata = {
    "State": "pending", #or "active" or "idle"
    "Title": "Seul la musique",
    "Artist": "unkown",
    "Album": "unkown", #should not be displayed
    "Status": "stopped", #or "playing"
    "Position" : "0x00000000 (0)", #(0)in ms
    "Duration": "0x00000000 (0)",
    "TrackNumber": "0x00000000 (0)", #should not be displayed
    "NumberOfTracks": "0x00000000 (0)", #should not be displayed
    "Volume": "0x0000 (0)",
    "Device": "unkown"
}

serial = i2c(port=1, address=0x3C)
device = sh1106(serial, rotate=0)

width = 128
height = 64

file = "/usr/src/app/logs.txt"

# prends le texte de logs.txt et le mets dans metadata
def getMetadata():
    txt = open(file, "r")
    lines = txt.readlines()
    for line in lines:
        key = line[:line.find(":")-1]
        value = line[line.find(":")+2:-1]
        metadata[key] = value
    txt.close()

# affiche le texte de logs.txt sur l'ecran
def displayMetadata():
    draw.text((0,0), metadata["Title"], fill="white")
    draw.text((0,10), metadata["Artist"], fill="white")
    draw.text((0,20), metadata["Album"], fill="white")
    draw.text((0,30), metadata["Status"], fill="white")
    draw.text((0,40), metadata["Position"], fill="white")
    draw.text((0,50), metadata["Duration"], fill="white")

i = 0
while(i<1000):
    with canvas(device) as draw:
        getMetadata()
        displayMetadata()
    i += 1