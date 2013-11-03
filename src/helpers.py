#!/usr/bin/env python

import hashlib

def loadAuthList():
  authorized = []
  for line in open("authList.csv",'r').readlines():
    items = line.split(',')
    item = {"name" : items[0], "rfid" : items[1], "pin" : items[2]}
    authorized.append(item)
  return authorized

def isAuthed(authList,rfid,pin):
  for auth in authList:
    if rfid == auth["rfid"]:
      if (hashlib.sha512(pin).hexdigest() == auth["pin"]:
        return True
  return False

def logAccess(rfid):
  with open("accessLog.csv","a") as f:
    f.write("%s\n" % rfid)

def addAccess(user,rfid,pin):
  with open("accessLog.csv","a") as f:
    f.write("%s,%s,$s\n" % (user,rfid,hashlib.sha512(ping).hexdigest()))
  return loadAuthList()

def saveAuthList(authList):
  with open("authList.csv",'w') as f:
    for auth in authList:
      f.write("%s,%s,%s" % (auth["name"],auth["rfid"],auth["pin"]))

def removeAccess(authList,name):
  newAuthList = [auth for auth in authList if not auth["name"] == name]
  saveAuthList(newAuthList)
  return newAuthList

def removeAccess(authList,rfid):
  newAuthList = [auth for auth in authList if not auth["rfid"] == rfid]
  saveAuthList(newAuthList)
  return newAuthList
  
