#!/usr/bin/env python
import time
import Flea
import FleaLanes
import FleaDriver
import random

minFleaBirth = 0.1
maxFleaBirth = 1.

minFleaInterval = 0.01
maxFleaInterval = .1

maxFleas = 5
minNumFleas = 5
maxNumFleas = 10

FleaTable = {}

debug = False
FleaCount=0
def addFlea():
  global FleaCount
  global maxFleas
  deadFleas=[]
  for flea in FleaTable:
    if FleaTable[flea].dead():
      if debug: print flea,"is dead"
      deadFleas.append(flea)
  for d in deadFleas:
    del FleaTable[d]
      
  FleaCount += 1
  if FleaCount == 1000:
    FleaCount = 0
  if FleaCount % 25 == 0:
    maxFleas = random.randint(minNumFleas,maxNumFleas)
    print "maxFleas:",maxFleas
  if len(FleaTable) < maxFleas:
    flea = Flea.Flea(str(FleaCount),random.uniform(minFleaInterval,maxFleaInterval))
    flea.setDaemon(True)
    FleaTable[flea.name]=flea
    FleaTable[flea.name].start()



if __name__ == '__main__':
  FleaDriver.setup()
  try:
    while True:
      addFlea()
      if debug: print "numFleas",len(FleaTable)
      wait = random.uniform(minFleaBirth,maxFleaBirth) 
      if debug: print "next flea:",wait
      time.sleep(wait)
  except KeyboardInterrupt:
    print "FleaWay exiting"
    FleaDriver.clear()
