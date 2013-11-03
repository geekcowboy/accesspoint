#!/usr/bin/env python

from rfid import RfidKeypad
import helpers

if __name__ == "__main__":
  rfid = RfidKeypad()

  username = raw_input()
  rfidKey = ''
  pin = ''

  try:
    while (rfidKey == ''):
      rfidKey = rfid.getRfid()
      sleep(0.2)

    print rfidKey
  
    key = None
    keys = []
    while (key != '#'):
      key = RfidKeypad.getKeyPress()
      if (key != None and key != '#'):
        keys.append(str(key))
      sleep(0.3)
    pin = ''.join(keys)
        
    helpers.addAccess(username,rfidKey,pin) 
  except KeyboardInterrupt:
    pass
