# 1.3" mono-colored oled display 128*64
# https://luma-oled.readthedocs.io/en/latest/

from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1325, ssd1331, sh1106
import time

from metadata import metadata

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
    draw.text((0, 0), metadata["Title"], fill="white")



def displayMusicDuration():
    timestampMs = metadata["Position"].split()
    timestampMs = timestampMs[1]
    durationMS = metadata["Duration"].split()
    durationMS = durationMS[1]
    
    draw.text((0, 0), ConvertMS(timestampMs) +"/"+ ConvertMS(durationMS), fill="white")

def displaySound():
    sound = metadata["Volume"]
    
    draw.text((0, 0), sound, fill="white")

def displayInit():
    with canvas(device) as draw:
        draw.text((0, 0), "Initialization", fill="white")


def displayTurningOff():
    with canvas(device) as draw:
        draw.text((0, 0), "Goodbye", fill="white")

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