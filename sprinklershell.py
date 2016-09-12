import time, JSON, datetime

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
