#test program to try out the display
#the point is to display hello world and such things in order to trivialize the rendering on the display.

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


with canvas(device) as draw:
    draw.text((0,0), "Hello, World!", fill="white")

time.sleep(10)



t = time.localtime()
current_time = time.strftime("%T", t)

print("main.py ended - " + current_time)