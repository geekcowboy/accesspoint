#!/usr/bin/env python

from rfid import RfidKeypad
from time import sleep
import helpers
import pdb

if __name__ == "__main__":
  rfid = RfidKeypad()
  
  authList = helpers.loadAuthList()

  loop = True
  while loop:
    try:
      rfidKey = rfid.getRfid()

      if rfidKey:
#        pdb.set_trace()
        helpers.logAccess(rfidKey)
        print rfidKey

        pin = helpers.getPin(rfid)
	if (rfidKey and pin):
          isAuth = helpers.isAuthed(authList,rfidKey,pin)
          if (isAuth):
            rfid.openDoorLock()
            rfidKey = ''
          else:
            rfid.flashRed()
            rfidKey = ''
      sleep(0.05)
    except KeyboardInterrupt:
      loop = False
