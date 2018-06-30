#!/usr/bin/env python
import time
import Flea
import FleaLanes
import FleaDriver
import random


minFleaInterval = 1
maxFleaInterval = 5

fleaCount = 5
fleaBump = 1
fleaGoal = 10
minNumFleas = 1
maxNumFleas = 30


FleaQuant=.0005

AddInterval = 1000

FleaTable = {}

debug = False
FleaCounter=0
def addFlea():
  global FleaCounter
  global fleaCount
  global fleaGoal
  global fleaBump
  deadFleas=[]
  for flea in FleaTable:
    if FleaTable[flea].dead():
      if debug: print flea,"is dead"
      deadFleas.append(flea)
  for d in deadFleas:
    del FleaTable[d]
      
  FleaCounter+= 1
  if FleaCounter % 100 == 0:
    fleaCount += fleaBump
    if fleaCount == fleaGoal:
      while fleaGoal == fleaCount:
        fleaGoal = random.randint(minNumFleas,maxNumFleas)
      if fleaCount < fleaGoal:
        fleaBump = 1
      else:
        fleaBump = -1

    print"fleaCount:",fleaCount,"fleaGoal",fleaGoal

  if len(FleaTable) < fleaCount:
    flea = Flea.Flea(str(FleaCounter),random.randint(minFleaInterval,maxFleaInterval))
    FleaTable[flea.name]=flea



if __name__ == '__main__':
  FleaDriver.setup()
  for i in range(fleaCount):
      addFlea()
  try:
    addCounter = 0
    while True:
      addFlea()
      for flea in FleaTable:
        FleaTable[flea].run()
      FleaDriver.flushIt()
      if debug: print "numFleas",len(FleaTable)
      if debug: print "next flea:",wait
      time.sleep(FleaQuant)
  except KeyboardInterrupt:
    print "FleaWay exiting"
    FleaDriver.clear()
