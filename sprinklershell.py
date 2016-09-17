# -*- coding: utf-8 -*-
import time, json, datetime, os, sys
from sprinklerhelperobj import SprinklerHelper

class ShellMenu():

    def ProgramBanner(self):
	os.system('clear')
        print "*********************************************************************************************"
        print "*******************************Mike's Sprinkler System Program*******************************"
        print "---------------------------------------------------------------------------------------------"
	time.sleep(1)

    def MainMenu(self):
	self.ProgramBanner()
	print "-------------------------------------------Main Menu-----------------------------------------"
	self.CurrentStatus()
	print "1 Manual Mode"
        print "2 Turn Auto Mode On/Off"
        print "3 Create Schedule"
        print "4 Quit"
        sel = raw_input("\nPlease choose 1 through 4 and press Enter\n> ")
	try:
          sel = int(sel)
          if sel == 1:
	    self.ManualMode()
	    self.MainMenu()
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
	  print "Scheduled On Time:\t", hour, ":", minute, "\n"
	  print "Scheduled Zones:\t", read.zones, "\n"

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
	  read.WriteStatusJSON(control, pump, zones, ontime)

    def ManualMode(self):
	zones = []
	done = False
	while not done:
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
	  zone = [pick, min]
	  print zone
	  zones.append([pick,min])
	  print zones
	  print "\nPick another zone?\n"
	  query = raw_input('Enter y or n > ')
	  if query == 'y': continue
	  else: break
	print zones
	if zones != []: control = "start"
	else: control = "manual"
	time.sleep(2)
	write = SprinklerHelper()
	write.WriteStatusJSON(control, False, zones, None)	

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
