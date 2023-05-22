#test program to try out the display
#the point is to display hello world and such things in order to trivialize the rendering on the display.

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

def displayTime():
    t = time.localtime()
    current_time = time.strftime("%T", t)
    draw.text((0,0), current_time, fill="white")

def displayPairingDevice():
    devicename = "device"
    draw.text((0, height-10), devicename, fill="white")


print("lancemant du script")
with canvas(device) as draw:
    displayTime()
    displayPairingDevice()

time.sleep(10)



t = time.localtime()
current_time = time.strftime("%T", t)

print("main.py ended - " + current_time)