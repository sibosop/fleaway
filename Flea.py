#!/usr/bin/env python
import random
import FleaLanes
from neopixel import Color

maxR = 60
maxG = 40
maxB = 20
     
debug = False
class Flea():
  def __init__(self,name,interval):
    self.isDead = False
    self.number = name
    self.name = "Flea"+name
    self.place = None
    self.interval = interval
    self.count=0
    self.color = {'r' : random.randint(0,maxR), 'g' : random.randint(0,maxG), 'b' : random.randint(0,maxB)}
    if debug: print("Starting Flea:"+self.name)
    
  def __str__(self):
    return "%02X" % self.color['r'] \
      + "%02X" % self.color['g'] \
      + "%02X" % self.color['b']
      
  def toColor(self):
    # seems to be grb
    return Color(self.color['g'],self.color['r'],self.color['b'])
    
  def dead(self):
    return self.isDead
    
  def kill(self):
    if debug: print self.name,"killed"
    self.isDead = True
    
  def move(self):
    if debug: print "-".rjust(8,"-")
    if FleaLanes.findPlace(self):
      self.kill()
    else:
      if debug: print self.name,"moved to:",str(self.place)
    if debug: print "-".rjust(8,"-")
    
  def run(self):
    if self.count < self.interval:
      self.count += 1
      return
    self.count = 0
    if not self.dead():
      self.move()
    else:
      if debug: print("Dead Flea:"+self.name)
        
      
