import RPi.GPIO as GPIO
import pygame
from time import sleep
import random

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN)

pygame.mixer.init()

sound = ["/audio/filepath",
         "/audio/filepath",
         "/audio/filepath",
         "/audio/filepath"
         ]


# motion detection 
while True:
    if GPIO.input(23):
        print("Detected!")
        audio = pygame.mixer.Sound(sound[random.randint(0, 3)])
        playing = audio.play()
        while playing.get_busy():
            pygame.time.delay(400)
        sleep(1)
    else:
        print("No Motion")
        sleep(1)