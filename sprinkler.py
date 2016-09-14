# Mike's Sprinkler System Object
# Written in python for the Raspberry Pi 3

import time, json, datetime
import RPi.GPIO as GPIO

class SprinklerSystem():
    def __init__(self):
        #variables
        self.pumpPin = 27 #Board 13
	self.l = [27,22,13,19,26,12,16,20] #list of BCM pin numbers in order from pump pin to zone7
        #initialize GPIO
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
	for x in self.l:
         GPIO.setup(x, GPIO.OUT)
         GPIO.output(x, GPIO.LOW)

    def ZoneToPin(self, zone): # Converts zone number to BCM pin number    
	if zone == 1: pin = 22 # Board 15
	elif zone == 2: pin = 13 # Board 33
	elif zone == 3: pin = 19 # Board 35
	elif zone == 4: pin = 26 # Board 37
	elif zone == 5: pin = 12 # Board 32
	elif zone == 6: pin = 16 # Board 36
	elif zone == 7: pin = 20 # Board 38
	return pin

    def WriteStatusJSON(self, control, pump, zones, ontime):
	update = {"control": control, "pump": pump, "zones": zones, "ontime": ontime}
	with open('status.json', 'w') as outfile:
	 json.dump(update, outfile)
	outfile.close()

    def ReadStatusJSON(self):
        with open('status.json') as infile:
	  data = json.load(infile)
        infile.close()
	return data

    def ReadScheduleJSON(self):
	with open('schedule.json') as infile:
	  sched = json.load(infile)
	infile.close()
	return sched

    def TurnZoneOn(self, zone, minutes, control, pump):
	now = time.time()
        finish = now + 60*minutes
	pin = self.ZoneToPin(zone)
        GPIO.output(pin, GPIO.HIGH)
	self.WriteStatusJSON(control, pump, zone, None)
	while now < finish:
          now = time.time()
          time.sleep(1)
        GPIO.output(pin, GPIO.LOW)

    def RunProgram(self, zones, control):
        GPIO.output(self.pumpPin, GPIO.HIGH)
	pump = True
	if all(isinstance(x, int) for x in zones):
	  zone = zones[0]
	  minutes = zones[1]
	  self.TurnZoneOn(zone, minutes, control, pump)	  
	elif all(isinstance(x, list) for x in zones):
	  for x in zones:
	   y = x
           zone = y[0]
	   minutes = y[1]
	   self.TurnZoneOn(zone, minutes, control, pump)
        GPIO.output(self.pumpPin, GPIO.LOW)
	pump = False
	zones = None 
	ontime = None
	self.WriteStatusJSON(control, pump, zones, ontime)

    def Run(self):
	while True:
	  data = self.ReadStatusJSON()
	  if str(data["control"]) == "start": 
	      zones = data["zones"]
	      control = "manual"
	      self.RunProgram(zones, control)
	  elif str(data["control"]) == "auto":
	      sched = self.ReadScheduleJSON()	
	      control = "auto"
	      zones = sched["zones"]
	      #Get ontime info here
	  else: time.sleep(5)

if __name__=="__main__": 
	sprunk = SprinklerSystem()
	sprunk.Run()
