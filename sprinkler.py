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
        GPIO.setmode(GPIO.BCM)
        GPIO.cleanup()
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

    def programBanner(self):
        print "**************************************************************************************"
        print "**************************Mike's Sprinkler System Program*****************************"
        print "--------------------------------------------------------------------------------------"

    def mainMenu(self):
        print "--------------------------------------Main Menu---------------------------------------"
        print "1 Manual Mode"
        print "2 Turn Auto Mode On/Off"
        print "3 Create Schedule"
        print "4 Quit"
        sel = raw_input("Please choose 1 through 4 and press Enter")
        if sel == 1: self.manualMode()
        elif sel == 2: self.autoOnOff()
        elif sel == 3: self.makeSchedule()
        elif sel == 4: self.close()
        else:
          print "Invalid selection. Select 1 through 4"
          self.mainMenu()
