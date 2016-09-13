#I wrote this code to test the pins on the GPIO board I'll be using
#for the sprinkler station
import RPi.GPIO as GPIO
import time

l = [5,6,13,19,26,12,16,20] #These are the BCM GPIO pin numbers
sec = .05 #Number of seconds each LED will be on
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
for y in l:
 GPIO.setup(y, GPIO.OUT)
 GPIO.output(y, GPIO.LOW)
for x in range(100):
 for y in l:
  GPIO.output(y, GPIO.HIGH)
  time.sleep(sec)
  GPIO.output(y, GPIO.LOW)
GPIO.cleanup()
