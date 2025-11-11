import RPi.GPIO as GPIO
from pydub import AudioSegment
from pydub.playback import play
from time import sleep
import random


GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)


#sample clips
sound = [
		AudioSegment.from_file("/audio/filepath", format="mp3"),
		AudioSegment.from_file("/audio/filepath", format="mp3"),	
		AudioSegment.from_file("/audio/filepath", format="mp3"),
		AudioSegment.from_file("/audio/filepath", format="mp3"),
		AudioSegment.from_file("/audio/filepath", format="mp3")				
		]


# motion detection 
try:
	while True:
		if GPIO.input(23):
			print("Detected!")
			play(random.choice(sound))
			sleep(1)
		else:
			print("No Motion")
			sleep(1)

except KeyboardInterrupt:
	GPIO.cleanup()
	pydub.quit()
