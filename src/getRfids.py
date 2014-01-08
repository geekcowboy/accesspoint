#!/usr/bin/env python

import serial
from subprocess import call
import time

port = serial.Serial('/dev/ttyAMA0',9600,timeout=1)

if port.isOpen() == False:
  port.open()

f = None

while True:
  try:
    if port.inWaiting():
      data = port.readline()
      curTime = time.clock()
      if len(data) > 5:
        output = "%s,%s\n" % (str(data).strip(),curTime)

        f = open('lastRfid.txt','w').write(output)
    time.sleep(0.01)
  except KeyboardInterrupt:
    port.close() 
    if f:
      f.close()
