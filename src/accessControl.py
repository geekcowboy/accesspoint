#!/usr/bin/env python

from rfid import RfidKeypad
from time import sleep
import helpers

if __name__ == "__main__":
  rfid = RfidKeypad()
  
  authList = helpers.loadAuthList()

  loop = True
  while loop:
    try:
      lastRfid = ''
      lastPin = ''
      rfidKey = rfid.getRfid()

      if rfidKey:
        helpers.logAccess(rfidKey)
        lastRfid = rfidKey
        print rfidKey

        currentPin = []
        curKeypad = None
        rfidCheck = rfid
        while curKeypad != '#' and (rfidCheck == rfidKey or rfidCheck == ''):
          curKeypad = rfid.getKeyPress()
          rfidCheck = rfid.getRfid()
          if (rfidCheck != ''):
            rfidKey = rfidCheck
            helpers.logAccess(rfidKey)

          if curKeyPad != None and curKeypad != '#' and (rfidCheck == '' or rfidCheck == rfidKey):
            currentPin.append(str(curKeyPad))
          elif rfidCheck != '' or rfidCheck != rfidKey:
            currentPin.clear()
            rfidKey = rfidCheck
            lastRfid = rfidKey
            break
          sleep(0.03)

        if (len(currentPin) > 0):
          lastPin =  ''.join(currentPin)
          print lastPin

	if (lastRfid and lastPin):
          isAuth = helpers.isAuthed(authList,lastRfid,lastPin)
          if (isAuthed):
            rfid.openDoorLock()
          else:
            rfid.flashRed()
      sleep(0.05)
    except KeyboardInterrupt:
      loop = False
