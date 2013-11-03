#!/usr/bin/env python

from matrix_keypad import RPi_GPIO as gpio
from time import sleep
from subprocess import call
import serial

class RfidKeypad:
  COLUMNS = [24,23,18]
  ROWS = [11,7,8,25]

  GREEN_LED = 9
  RED_LED = 10
  DOOR_LOCK = 22

  lastRFID = ''
  lastKey = ''
  
  def __init__(self):
    call(["gpio", "reset"])

    self.kb = gpio.keypad(columnCount = 3)
    self.kb.COLUMN = self.COLUMNS
    self.kb.ROW = self.ROWS
    
    port = serial.Serial("/dev/ttyAMA0", baudrate=9600)
    
    gpio.GPIO.setup(self.GREEN_LED,gpio.GPIO.OUT)
    gpio.GPIO.output(self.GREEN_LED,gpio.GPIO.LOW)
    gpio.GPIO.setup(self.RED_LED,gpio.GPIO.OUT)
    gpio.GPIO.output(self.RED_LED,gpio.GPIO.LOW)
    gpio.GPIO.setup(self.DOOR_LOCK,gpio.GPIO.OUT)
    gpio.GPIO.output(self.DOOR_LOCK,gpio.GPIO.LOW)

  def __enter__(self):
    return self;

  def __exit__(self, type, value, traceback):
    gpio.GPIO.cleanup()

  def changePinState(self,pin,state):
    gpio.GPIO.output(pin,state)

  def turnOnGreen(self):
    self.changePinState(self.GREEN_LED,gpio.GPIO.HIGH)

  def turnOffGreen(self):
    self.changePinState(self.GREEN_LED,gpio.GPIO.LOW)

  def flashGreen(self,timeToFlash=1):
    self.turnOnGreen()
    sleep(timeToFlash)
    self.turnOnGreen()

  def turnOnRed(self):
    self.changePinState(self.RED_LED,gpio.GPIO.HIGH)

  def turnOffRed(self):
    self.changePinState(self.RED_LED,gpio.GPIO.LOW)

  def flashRed(self,timeToFlash=1):
    self.turnOnRed()
    sleep(timeToFlash)
    self.turnOnRed()

  def openDoorLock(self,timeToFlash=1):
    self.turnOnGreen()
    self.changePinState(self.DOOR_LOCK,gpio.GPIO.HIGH)
    sleep(timeToFlash)
    self.changePinState(self.DOOR_LOCK,gpio.GPIO.LOW)
    self.turnOffGreen()

  def getKeyPress(self):
    key = self.kb.getKey()
    return key

  def getRfid(self):
    key = ''
    numBytes = self.port.isWaiting()
    if numBytes > 0:
      key = self.port.read(numBytes)
    return key

if __name__ == "__main__":
  rfid = RfidKeypad()

  loop = True
  while loop:
    try:
      rfidKey = rfid.getRfid()
      if rfidKey:
        print rfidKey
  
      curKeypad = rfid.getKeyPress()
      if (curKeyPad != None):
        print curKeyPad
      
      sleep(0.1)
    except KeyboardInterrupt:
      loop = False
