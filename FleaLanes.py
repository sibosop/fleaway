#!/usr/bin/env python
import Flea
import random
import FleaDriver
from neopixel import Color


MaxLanes = 3
MaxSlots = 72
LaneTable = []

debug=False


class Place:
  def __init__(self,l,p):
    self.flea = None
    self.pos = {}
    self.pos['lane'] = l
    self.pos['slot'] = p
    
  def empty(self):
    return self.flea == None
  
  def lane(self):
    return self.pos['lane']
  
  def slot(self):
    return self.pos['slot']
    
  def toPos(self):
    rval = 0
    if self.lane() % 2:
      #odd lanes are backwards
      rval=(self.lane()*MaxSlots)+(MaxSlots-self.slot()-1)
    else:
      rval = (self.lane() * MaxSlots) + self.slot()
    return rval
    
    
    
  def clear(self):
    FleaDriver.queueVal(self.toPos(),Color(0,0,0))
    self.flea = None
    
  def show(self):
    if self.flea != None:
      return self.flea.number.ljust(4)
    return "-".ljust(4)
   
  def __str__(self):
    if debug: print self.pos['lane'],":",self.pos['slot']
    val = self.pos['lane'] << 6
    val |= self.pos['slot']
    return "%02X" % val
    
def setPlace(flea,place):
  if flea.place != None:
    flea.place.clear()
  flea.place = place
  place.flea = flea
  if place != None:
    FleaDriver.queueVal(place.toPos(),flea.toColor())
    
def findPlace(flea):
  touched = True
  rval = False
  if flea.place == None:
    t = False
    emptys = []
    for i in range(MaxLanes-1,-1,-1):
      if LaneTable[i][0].empty():
        emptys.append(i)
    if len(emptys) != 0:
      setPlace(flea,LaneTable[random.choice(emptys)][0])
  
      t = True
    touched = t
  else:
    lane = flea.place.lane()
    slot = flea.place.slot()
    nextSlot = slot + 1
    # look ahead straight
    if nextSlot == MaxSlots:
      LaneTable[lane][slot].clear()
      touched = True
      rval = True
    elif LaneTable[lane][nextSlot].empty():
      setPlace(flea,LaneTable[lane][nextSlot])
      touched = True
    elif lane != 0 and LaneTable[lane-1][nextSlot].empty():
      setPlace(flea,LaneTable[lane-1][nextSlot])
      touched = True
    elif (lane+1) != MaxLanes and LaneTable[lane+1][nextSlot].empty():
      setPlace(flea,LaneTable[lane+1][nextSlot])
      touched = True
  
  #if touched:
    #FleaDriver.flushIt()
    #dump()
  return rval
  
def dump():
  for lane in LaneTable:
    d = ""
    for place in lane:
      d += place.show() + " "
    print d    
    
for lane in range(MaxLanes):
  LaneTable.append([])
  for slot in range(MaxSlots):
    LaneTable[-1].append(Place(lane,slot))
  


    
