# -*- coding: utf-8 -*-
import time, json, datetime, os, sys
from sprinklerhelperobj import SprinklerHelper

class ShellMenu():

    def ProgramBanner(self):
	os.system('clear')
        print "**************************************************************************************"
        print "**************************Mike's Sprinkler System Program*****************************"
        print "--------------------------------------------------------------------------------------"
	time.sleep(1)

    def MainMenu(self):
        print "--------------------------------------Main Menu---------------------------------------"
        print "1 Manual Mode"
        print "2 Turn Auto Mode On/Off"
        print "3 Create Schedule"
        print "4 Quit"
        sel = raw_input("Please choose 1 through 4 and press Enter\n")
	try:
	 sel = int(sel)
         if sel == 1: print 'Yeah!'
         elif sel == 2: print 'What?!'
         elif sel == 3: print 'OK!'
         elif sel == 4: self.close()
         else:
	   self.fuckyou()
           self.MainMenu()
	except:
	 self.fuckyou()
	 self.MainMenu()

    def AutoOnOff(self):
	read = SprinklerHelper()
	read.ReadStatusJSON()
	if read.control == "auto":
	   print "Auto is currently turned on. Would you like to turn it off?\n"
	   turnon = raw_input("Enter y or n > ")
	   if turnon == 'y':
	      print "holla"	
	      
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
	shelly.ProgramBanner()
	shelly.MainMenu()
