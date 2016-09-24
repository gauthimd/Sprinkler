# -*- coding: utf-8 -*-
import time, json, datetime, os, sys
from sprinklerhelperobj import SprinklerHelper

class ShellMenu():

    def __init__(self):
	self.daydict = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}

    def ProgramBanner(self):
	os.system('clear')
        print "***************************************************************************************************************"
        print "***************************************Mike's Sprinkler System Program*****************************************"
        print "---------------------------------------------------------------------------------------------------------------"
	time.sleep(1)

    def MainMenu(self):
	self.ProgramBanner()
	print "---------------------------------------------------Main Menu---------------------------------------------------"
	time.sleep(1)
	self.CurrentStatus()
	time.sleep(1)
	print "\n1 Manual Mode"
        print "2 Turn Auto Mode On/Off"
        print "3 Create Schedule"
	print "4 Update Status"
        print "5 Quit"
        sel = raw_input("\nPlease choose 1 through 5 and press Enter\n> ")
	try:
	  a = int(sel)
	except: a = 0
	if 1 <= a <= 5:
          if a == 1:
	    self.ManualMode()
	    self.MainMenu()
          elif a == 2: 
	    self.AutoOnOff()
	    self.MainMenu()
          elif a == 3: 
	    self.ScheduleMode()
	    self.MainMenu()
	  elif a == 4: self.MainMenu()
          elif a == 5: self.close()
	else:
	  self.fuckyou()
	  self.MainMenu()

    def CurrentStatus(self):
        read = SprinklerHelper()
	read.ReadStatusJSON()
	if read.ontime != None:
	  ontime = '{0}:{1}'.format('%02d' % read.hour, '%02d' % read.minute)
	else: ontime = read.ontime
	if read.pump == True: pump = 'On'
	else: pump = 'Off'
	print "\nCurrent Status:\t\t\t| Control Mode: ", read.control, "| Pump: ", pump, "| Zone: ", read.zones, "| On time: ", ontime, "|"
	now = datetime.datetime.now()
        print "\nCurrent Date/Time:\t\t", now.ctime()
	if read.control == "Auto":
	  read.ReadScheduleJSON()
	  daylist = []
	  for x in read.weekdays: daylist.append(self.daydict[x])
	  hour, minute = read.ontime[0], read.ontime[1]
	  print "\nScheduled On Time:\t\t", "{0}:{1}".format('%02d' % hour, '%02d' % minute)
	  print "\nScheduled [[Zone, Minutes]]:\t", read.zones
	  print "\nScheduled Weekdays:\t\t", daylist

    def AutoOnOff(self):
	read = SprinklerHelper()
	read.ReadStatusJSON()
	pump = read.pump
	zones = read.zones
	ontime = read.ontime
	if read.control ==  "Auto":
	  control = "Manual"
	  read.WriteStatusJSON(control, pump, zones, ontime)
	else:
	  control = "Auto"
	  read.WriteStatusJSON(control, pump, zones, ontime)

    def ScheduleMode(self):
	read = SprinklerHelper()
	read.ReadScheduleJSON()
	oldsched = read.weekdays
	self.day = []
	while True:
	  print "\nPick a day of the week you would like the sprinkler to turn on."
	  day = raw_input("Enter 1 through 7 (1=Monday, 2=Tuesday, 3=Wednesday, 4=Thursday, 5=Friday, 6=Saturday, 7=Sunday)\n> ")
	  try:
	    day = int(day)
	    if not 1 <= day <= 7:
	      self.fuckyou()
	      break
	  except:
	    self.fuckyou()
	    break
	  self.day.append(day)
	  daylist = []
	  for x in self.day: daylist.append(self.daydict[x])
	  print "\n", daylist
	  print "\nPick another day?"
	  another = raw_input("Enter y or n\n> ")
	  if another == 'y': continue
	  else: pass
	  set = raw_input("\nWhat hour would you like it to turn on? Enter 0-23\n> ")
	  try:
	    set = int(set)
	    if not 0 <= set <= 23:
	      self.fuckyou()
	      break
	  except:
	    self.fuckyou()
	    break
	  minute = raw_input("\nWhat minute would you like it to turn on? Enter 0-59\n> ")
	  try:
	    minute = int(minute)
	    if not 0 <= minute <= 59:
	      self.fuckyou()
   	      break
	  except:
	    self.fuckyou()
	    break
	  self.setontime = [set, minute]
	  self.PickZones()
	  if self.zones != [] and self.zones != None:
	    if all(isinstance(x, int) for x in self.setontime):
	      if all(isinstance(x, int) for x in self.day):
		print "\nSchedule accepted"
	 	time.sleep(2)
                read.WriteScheduleJSON(self.day, self.setontime, self.zones)
	        break 	 
	      else: 
		self.fuckyou()
	        break
	    else: 
		self.fuckyou()
		break
	  else: 
	    self.fuckyou()
	    break

    def PickZones(self):
	self.zones = []
	read = SprinklerHelper()
	read.ReadStatusJSON()
	old = read.zones
	self.control = read.control
	self.pump = read.pump
	self.ontime = read.ontime
	min = 'd'
	while True:
  	  print "\nWhat zone would you like to turn on?"
	  pick = raw_input('Enter 1 through 7 > ')
	  try:
	    pick = int(pick)
	    if not 1 <= pick <= 7:
	      self.fuckyou()
	      break
	  except:
	    self.fuckyou()
	    break
	  print "\nHow many minutes would you like it to come on for?"
	  min = raw_input("Enter 1 though 90 > ")
	  try:
	    min = int(min)
	    if not 1 <= min <= 90:
	      self.fuckyou()
	      break
	  except:
  	    self.fuckyou()
	    break
	  self.zones.append([pick,min])
	  print "\n[[Zone, minutes]]: ", self.zones
	  print "\nPick another zone?"
	  query = raw_input('Enter y or n > ')
	  if query == 'y': continue
	  else: break
	if isinstance(min, int): 
	  if self.control == "Manual":
	    self.control = "Start"
	  now = datetime.datetime.now()
	  hour = int(now.hour)
	  minute = int(now.minute)
	  self.ontime = [hour, minute]
	else: 
	  self.zones = old

    def ManualMode(self):
	write = SprinklerHelper()
	write.ReadStatusJSON()
	if write.control == "Auto":
	  self.control = "Manual"
	  write.ReadStatusJSON()
	  self.pump = write.pump
	  self.zones = write.zones
	  self.ontime = write.ontime
	  write.WriteStatusJSON(self.control, self.pump, self.zones, self.ontime)
	self.PickZones()
	write.WriteStatusJSON(self.control, self.pump, self.zones, self.ontime)	
	print "\nTurning sprinklers on..."
	time.sleep(3)

    def fuckyou(self):
	os.system('clear')
	print """
		....................../´¯/) 
		....................,/¯../ 
		.................../..../ 
		............./´¯/'...'/´¯¯`·¸ 
		........../'/.../..../......./¨¯\ 
		........('(...´...´.... ¯~/'...') 
		.........\.................'...../ 
		..........''...\.......... _.·´ 
		............\..............( 
		..............\.............\...   """
	time.sleep(2)
	os.system('clear')

    def close(self):
	os.system('exit')

if __name__=="__main__":
	shelly = ShellMenu()
	shelly.MainMenu()
