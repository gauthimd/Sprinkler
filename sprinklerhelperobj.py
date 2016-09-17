import json

class SprinklerHelper():

    def WriteStatusJSON(self, control, pump, zones, ontime):
	update = {"control": control, "pump": pump, "zones": zones, "ontime": ontime}
	with open('status.json', 'w') as outfile:
	  json.dump(update, outfile)
	outfile.close()

    def ReadStatusJSON(self):
	with open('status.json') as infile:
	  data = json.load(infile)
	infile.close()
	self.control = data["control"]
	self.zones = data["zones"]
	self.pump = data["pump"]
	self.ontime = data["ontime"]
	if self.ontime != None:
	  self.hour = self.ontime[0]
	  self.minute = self.ontime[1]

    def ReadScheduleJSON(self):
	with open('schedule.json') as infile:
	  sched = json.load(infile)
	infile.close()
	self.weekdays = sched["weekdays"]
	self.ontime = sched["ontime"]
	self.hour = self.ontime[0]
	self.minute = self.ontime[1]
	self.zones = sched["zones"]
	return sched

