# Mike's Sprinkler System Object written in python for the Raspberry Pi 3

import time, json, datetime
import RPi.GPIO as GPIO
from sprinklerhelperobj import SprinklerHelper

class SprinklerSystem():

    def __init__(self):
        self.pumpPin = 27 #Board 13
	self.zonedict = {1:22, 2:13, 3:19, 4:26, 5:12, 6:16, 7:20} # {zone:pin}
	self.l = [27,22,13,19,26,12,16,20] #list of BCM pin numbers in order from pump pin to zone7
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
	for x in self.l:
         GPIO.setup(x, GPIO.OUT)
         GPIO.output(x, GPIO.HIGH)

    def TurnZoneOn(self, zone, minutes, pump):
	now = time.time()
        finish = now + 60*minutes
	pin = self.zonedict.get(zone)
        GPIO.output(pin, GPIO.LOW)
	nowtime = datetime.datetime.now()
	hour = nowtime.hour
	min = nowtime.minute
	ontime = [hour, min]
	read = SprinklerHelper()
	read.ReadStatusJSON()
	control = read.control
	write = SprinklerHelper()
	write.WriteStatusJSON(control, pump, zone, ontime)
	while now < finish:
          now = time.time()
          time.sleep(1)
        GPIO.output(pin, GPIO.HIGH)

    def RunProgram(self, zones, control):
        GPIO.output(self.pumpPin, GPIO.LOW)
	pump = True
	write = SprinklerHelper()
	write.WriteStatusJSON(control, pump, zones, None)
	if all(isinstance(x, int) for x in zones):
	  zone = zones[0]
	  minutes = zones[1]
	  self.TurnZoneOn(zone, minutes, pump)	  
	elif all(isinstance(x, list) for x in zones):
	  for x in zones:
	   y = x
           zone = y[0]
	   minutes = y[1]
	   self.TurnZoneOn(zone, minutes, pump)
        GPIO.output(self.pumpPin, GPIO.HIGH)
	pump = False
	zones = None 
	ontime = None
	write.ReadStatusJSON()
	control = write.control
	write.WriteStatusJSON(control, pump, zones, None)

    def Run(self):
	while True:
	  read = SprinklerHelper()
	  read.ReadStatusJSON()
	  control = read.control
	  if control == "Start":
	      zones = read.zones
	      control = "Manual"
	      self.RunProgram(zones, control)
	  elif control == "Auto":
	      read.ReadScheduleJSON()
	      now = datetime.datetime.now()
	      today = datetime.date.isoweekday(now)
	      weekdays = read.weekdays 
	      hour = read.hour
	      minute = read.minute
	      if today in weekdays:
		if now.hour == hour and now.minute == minute:
		  zones = read.zones
		  self.RunProgram(zones, control)
		else: time.sleep(5)
	      else: time.sleep(5)
	  else: time.sleep(5)

if __name__=="__main__": 
	sprunk = SprinklerSystem()
	sprunk.Run()
