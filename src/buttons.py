import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)

ButtonData = "/shared/logs/data.log"

while True:
    input_stateA = GPIO.input(17) # enabling bluetooth logs button
    input_stateB = GPIO.input(18) 
    input_stateC = GPIO.input(19)
    input_stateD = GPIO.input(20)
    input_stateE = GPIO.input(21) # restart pair button


    if input_stateA == False:
        #if button A pressed
        print('Button A Pressed')
        if os.path.exists(ButtonData) == True:
            txt = open(ButtonData, "r")
            txt.write("State: 1")

            txt.close()

    if input_stateE == False:
        #if button E pressed
        print('Button E Pressed')
        if os.path.exists(ButtonData) == True:
            txt = open(ButtonData, "r")
            txt.write("Reset: 1")
            txt.close()