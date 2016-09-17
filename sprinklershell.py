# -*- coding: utf-8 -*-
import time, json, datetime, os, sys
from sprinklerhelperobj import SprinklerHelper

class ShellMenu():

    def ProgramBanner(self):
	os.system('clear')
        print "****************************************************************************************"
        print "****************************Mike's Sprinkler System Program*****************************"
        print "----------------------------------------------------------------------------------------"
	time.sleep(1)

    def MainMenu(self):
	self.ProgramBanner()
	print "----------------------------------------Main Menu---------------------------------------"
	self.CurrentStatus()
	print "1 Manual Mode"
        print "2 Turn Auto Mode On/Off"
        print "3 Create Schedule"
        print "4 Quit"
        sel = raw_input("\nPlease choose 1 through 4 and press Enter\n> ")
	try:
          sel = int(sel)
          if sel == 1: print 'Yeah!'
          elif sel == 2: 
	    self.AutoOnOff()
	    self.MainMenu()
          elif sel == 3: print 'OK!'
          elif sel == 4: self.close()
	  else:
	    self.fuckyou()
	    self.MainMenu()
	except:
	  self.fuckyou()
	  self.MainMenu()

    def CurrentStatus(self):
        read = SprinklerHelper()
	read.ReadStatusJSON()
	now = datetime.datetime.now()
	print "\nCurrent Status:    | Control Mode: ", read.control, "| Pump: ", read.pump, "| Zone: ", read.zones, "| On time: ", read.ontime, "|\n"
        print "\nCurrent Time:    ", now.ctime(), "\n"
	if read.control == "auto":
	  read.ReadScheduleJSON()
	  hour, minute = read.ontime[0], read.ontime[1]
	  print "Scheduled On Time:    ", hour, ":", minute, "\n"

    def AutoOnOff(self):
	read = SprinklerHelper()
	read.ReadStatusJSON()
	pump = read.pump
	zones = read.zones
	ontime = read.ontime
	if read.control ==  "auto":
	  control = "manual"
	  read.WriteStatusJSON(control, pump, zones, ontime)
	else:
	  control = "auto"
	  read.WriteStatusJSON(control, pump,zones, ontime)

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
