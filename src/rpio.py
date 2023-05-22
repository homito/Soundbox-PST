import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN)

# Ajout des boutons généraux
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Bouton pour l'alimentation de la raspberry pi
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Bouton pour les LEDS

# Variable pour enregistrer l'état des boutons
power_button_state = False
led_button_state = False

# Variables pour enregistrer l'état des LEDS
led_blue = False
led_red = False
led_green = False

while True:
    volume = GPIO.input(18)
    os.system("volume du son {}%".format(volume * 100))

    # Gestion du bouton d'alimentation de la raspberry pi
    input_power_button = GPIO.input(23)
    if not input_power_button and not power_button_state:
        power_button_state = True
        #allumer ou éteindre la raspberry pi
        os.system("sudo shutdown -h now")

    elif input_power_button and power_button_state:
        power_button_state = False

    # Gestion du bouton pour les LEDS
    input_led_button = GPIO.input(24)
    if not input_led_button and not led_button_state:
        led_button_state = True
        #allumer et éteindre les LEDS en bleu, rouge et vert
        if not led_blue:
            led_blue = True
            # Code pour allumer les LEDS en bleu
        elif led_blue and not led_red:
            led_red = True
            # Code pour allumer les LEDS en rouge
        elif led_red and not led_green:
            led_green = True
            # Code pour allumer les LEDS en vert
        else:
            led_blue = False
            led_red = False
            led_green = False
            # Code pour éteindre les LEDS

    elif input_led_button and led_button_state:
        led_button_state = False

    #time.sleep(0.1)

GPIO.cleanup()

#Ce code utilise la bibliothèque RPi.GPIO pour contrôler les entrées des broches
#GPIO de la Raspberry Pi et la fonction os.system() pour exécuter des commandes shell qui ajustent le volume audio en utilisant ALSA 
#(Advanced Linux Sound Architecture).

#Remarque: veuillez vous assurer que le numéro de broche 18 utilisé dans ce code correspond bien à la
#broche sur laquelle le potentiomètre est connecté.