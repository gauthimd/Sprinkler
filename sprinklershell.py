# -*- coding: utf-8 -*-
import time, json, datetime, os, sys
from sprinklerhelperobj import SprinklerHelper

class ShellMenu():

    def ProgramBanner(self):
	os.system('clear')
        print "*********************************************************************************************"
        print "*******************************Mike's Sprinkler System Program*******************************"
        print "---------------------------------------------------------------------------------------------"
	time.sleep(2)

    def MainMenu(self):
	self.ProgramBanner()
	print "-------------------------------------------Main Menu-----------------------------------------"
	self.CurrentStatus()
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
	print "\nCurrent Status:    | Control Mode: ", read.control, "| Pump: ", pump, "| Zone: ", read.zones, "| On time: ", ontime, "|\n"
	now = datetime.datetime.now()
        print "\nCurrent Date/Time:\t\t", now.ctime()
	if read.control == "Auto":
	  read.ReadScheduleJSON()
	  hour, minute = read.ontime[0], read.ontime[1]
	  print "\nScheduled On Time:\t\t", "{0}:{1}".format('%02d' % hour, '%02d' % minute)
	  print "\nScheduled [[Zone, Minutes]]:\t", read.zones, "\n"

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
	pass

    def ManualMode(self):
	zones = []
	read = SprinklerHelper()
	read.ReadStatusJSON()
	old = read.zones
	control = read.control
	pump = read.pump
	ontime = read.ontime
	min = 'd'
	while True:
  	  print "\nWhat zone would you like to turn on?\n"
	  pick = raw_input('Enter 1 through 7 > ')
	  try:
	    pick = int(pick)
	    if not 1 <= pick <= 7:
	      self.fuckyou()
	      break
	  except:
	    self.fuckyou()
	    break
	  print "\nHow many minutes would you like it to come on for? \n"
	  min = raw_input("Enter 1 though 60 > ")
	  try:
	    min = int(min)
	    if not 1 <= min <= 60:
	      self.fuckyou()
	      break
	  except:
  	    self.fuckyou()
	    break
	  zones.append([pick,min])
	  print "\nZones: ", zones
	  print "\nPick another zone?\n"
	  query = raw_input('Enter y or n > ')
	  if query == 'y': continue
	  else: break
	if isinstance(min, int): 
	  control = "Start"
	  now = datetime.datetime.now()
	  hour = int(now.hour)
	  minute = int(now.minute)
	  ontime = [hour, minute]
	else: 
	  zones = old
	write = SprinklerHelper()
	write.WriteStatusJSON(control, pump, zones, ontime)	
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
