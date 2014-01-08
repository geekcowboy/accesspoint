#!/usr/bin/env python

from rfid import RfidKeypad
from time import sleep
import helpers

if __name__ == "__main__":
  rfid = RfidKeypad()

  print "Enter the user name: "
  username = raw_input()
  print "Username = %s\n" % username
  rfidKey = ''
  pin1 = ''
  pin2 = ''
  pinsMatch = False

  try:
    print "Scan RFID"
    while (rfidKey == ''):
      rfidKey = rfid.getRfid()
      sleep(0.2)

    print "RFID read as: %s\n" % rfidKey
  
    while (pinsMatch == False):
      print "Enter Pin: "
      pin1 = helpers.getPin(rfid,True)
      print "Enter Pin Again: "
      pin2 = helpers.getPin(rfid,True)
      if pin1 == pin2 and pin1 != '':
        pinsMatch = True
      else:
        print "Pins do not match, try again!"

    helpers.addAccess(username,rfidKey,pin1) 
    
    print "User Added"

    rfid.openDoorLock()
  except KeyboardInterrupt:
    pass
