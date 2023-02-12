# 1.3" mono-colored oled display 128*64
# https://luma-oled.readthedocs.io/en/latest/

from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1325, ssd1331, sh1106
import time

serial = i2c(port=1, address=0x3C)
device = sh1106(serial, rotate=0)

width = 128
height = 64

def displayParingWait():
    isPaired = 0
    
    with canvas(device) as draw:
        draw.text((0, 0), "Waiting for pairing", fill="white")
        while (isPaired == 0):
            print("waiting for device pair")
        print("device found")
        return 1

def displayPairingDevice():
    devicename = "device"
    draw.text((0, 0), devicename, fill="white")

def displayTime():
    t = time.localtime()
    current_time = time.strftime("%H:%M", t)
    draw.text((0, 0), current_time, fill="white")

    

def displayService():
    service = "Spotify"
    draw.text((0, 0), service, fill="white")

def displayMusicName():
    name = "never gonna give you up - Rick Astley"
    draw.text((0, 0), name, fill="white")



def displayMusicDuration():
    draw.text((0, 0), "hh:mm:ss/hh:mm:ss", fill="white")

def displaySound():
    sound = 69
    draw.text((0, 0), sound, fill="white")

def displayInit():
    with canvas(device) as draw:
        draw.text((0, 0), "Initialization", fill="white")


def displayTurningOff():
    with canvas(device) as draw:
        draw.text((0, 0), "Goodbye", fill="white")

# -------- 
displayInit()

devicePaired = 0
soundChange = 0

while devicePaired == 0:
    print("waiting for pair")
print("device paired")

while(1):
    displayTime()
    displayService()
    displayMusicName()
    displayPairingDevice()

    if(soundChange == 1):
        displaySound()
    displayMusicDuration()