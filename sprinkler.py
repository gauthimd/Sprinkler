import time, JSON, datetime
import RPi.GPIO as GPIO

class SprinklerSystem():
    def __init__(self):
        #variables
        self.auto = False
        self.pumpPin = 5 #Board 29
        self.zone1Pin = 6 #Board 31
        self.zone2Pin = 13 #Board 33
        self.zone3Pin = 19 #Board 35
        self.zone4Pin = 26 #Board 37
        self.zone5Pin = 12 #Board 32
        self.zone6Pin = 16 #Board 36
        self.zone7Pin = 20 #Board 38
        #initialize GPIO
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pumpPin, GPIO.OUT)
        GPIO.setup(self.zone1Pin, GPIO.OUT)
        GPIO.setup(self.zone2Pin, GPIO.OUT)
        GPIO.setup(self.zone3Pin, GPIO.OUT)
        GPIO.setup(self.zone4Pin, GPIO.OUT)
        GPIO.setup(self.zone5Pin, GPIO.OUT)
        GPIO.setup(self.zone6Pin, GPIO.OUT)
        GPIO.setup(self.zone7Pin, GPIO.OUT)
        GPIO.output(self.pumpPin, GPIO.LOW)
        GPIO.output(self.zone1Pin, GPIO.LOW)
        GPIO.output(self.zone2Pin, GPIO.LOW)
        GPIO.output(self.zone3Pin, GPIO.LOW)
        GPIO.output(self.zone4Pin, GPIO.LOW)
        GPIO.output(self.zone5Pin, GPIO.LOW)
        GPIO.output(self.zone6Pin, GPIO.LOW)
        GPIO.output(self.zone7Pin, GPIO.LOW)
	#todo: init status json object and write to status.json

    def TurnAutoOn(self):
        self.auto = True
        #update status.json

    def TurnAutoOff(self):
        self.auto = False
        #update status.json

    def ManualModeOn(self, zone, minutes):
        now = time.localtime()
        finish = time.localtime() + 60*minutes
        while now < finish:
          GPIO.output(self.pumpPin, GPIO.HIGH)
          GPIO.output(zone, GPIO.HIGH)
          now = time.localtime()
          time.sleep(1)
          #update status.json
        GPIO.output(self.pumpPin, GPIO.LOW)
        GPIO.output(zone, GPIO.LOW)