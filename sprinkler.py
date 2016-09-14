import time, json, datetime
import RPi.GPIO as GPIO

class SprinklerSystem():
    def __init__(self):
        #variables
        self.pumpPin = 27 #Board 13
        self.zone1Pin = 22 #Board 15
        self.zone2Pin = 13 #Board 33
        self.zone3Pin = 19 #Board 35
        self.zone4Pin = 26 #Board 37
        self.zone5Pin = 12 #Board 32
        self.zone6Pin = 16 #Board 36
        self.zone7Pin = 20 #Board 38
	self.l = [27,22,13,19,26,12,16,20] #list of BCM pin numbers in order from pump pin to zone7
        #initialize GPIO
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
	for x in self.l:
         GPIO.setup(x, GPIO.OUT)
         GPIO.output(x, GPIO.LOW)

    def RunProgram(self, zones):
        GPIO.output(self.pumpPin, GPIO.HIGH)
	zone = zones[0]
	minutes = zones[1]
	now = time.time()
        finish = now + 60*minutes
        GPIO.output(zone, GPIO.HIGH)
        update = {"control": None, "pump": True, "zones": zone}
	with open('status.json', 'w') as outfile:
	 json.dump(update, outfile)
	outfile.close()
	while now < finish:
          now = time.time()
          time.sleep(1)
        GPIO.output(zone, GPIO.LOW)
        GPIO.output(self.pumpPin, GPIO.LOW)

    def Run(self):
	while True:
 	  with open('status.json') as infile:
	      data = json.load(infile)
  	  infile.close()
	  if str(data["control"]) == "manual": 
	      zones = data["zones"]
	      self.RunProgram(zones)
	  elif str(data["control"]) == "auto":
	      with open('schedule.json') as infile:
		  data = json.load(infile)
              infile.close()
	      #Get ontime info here
	  else: time.sleep(5)

if __name__=="__main__": 
	sprunk = SprinklerSystem()
	sprunk.Run()
