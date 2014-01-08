#!/usr/bin/env python

import hashlib
from time import sleep

def loadAuthList():
  authorized = []
  for line in open("authList.csv","r+").readlines():
    items = line.strip().split(',')
    item = {"name" : items[0], "rfid" : items[1], "pin" : items[2]}
    authorized.append(item)
  return authorized

def isAuthed(authList,rfid,pin):
  for auth in authList:
    if rfid == auth["rfid"]:
      pinHash = hashlib.sha512(str(pin)).hexdigest()
      if  pinHash == auth["pin"]:
        return True
      else:
        return False
  return False

def logAccess(rfid):
  with open("accessLog.csv","a+") as f:
    f.write("%s\n" % rfid)

def addAccess(user,rfid,pin):
  with open("authList.csv","a+") as f:
    f.write("%s,%s,%s\n" % (user,rfid,hashlib.sha512(pin).hexdigest()))
  return loadAuthList()

def saveAuthList(authList):
  with open("authList.csv",'w+') as f:
    for auth in authList:
      f.write("%s,%s,%s" % (auth["name"],auth["rfid"],auth["pin"]))

def removeAccessByName(authList,name):
  newAuthList = [auth for auth in authList if not auth["name"] == name]
  saveAuthList(newAuthList)
  return newAuthList

def removeAccessByRfid(authList,rfid):
  newAuthList = [auth for auth in authList if not auth["rfid"] == rfid]
  saveAuthList(newAuthList)
  return newAuthList
  
def getPin(rfidKeypad,printKey = False):
  key = None
  keys = []
  while (key != '#'):
    key = rfidKeypad.getKeyEntry()
    if (key != '#'):
      if (key):
        keys.append(str(key))
        key = None
        if printKey:
          print "*"
  return ''.join(keys)


