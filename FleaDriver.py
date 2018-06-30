#!/usr/bin/env python
import subprocess
from neopixel import Color

# LED strip configuration:
LED_COUNT      = 288      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53


debug = False

def isMac():
  rval = False
  mach = subprocess.check_output(["uname"]).rstrip()
  if mach == "Darwin":
    rval = True
  return rval

if not isMac():
  from neopixel import *

strip = None
def setup():
  global strip
  if not isMac():
    print "not mac"
    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()

buff = []
def queueVal(pos,color):
  global buff
  if debug: print "queueing",pos,color
  buff.append({'pos':pos,'color':color})
  
def clear():
  global strip
  for i in range(strip.numPixels()):
      strip.setPixelColor(i, Color(0,0,0))
  strip.show()
  
  
def flushIt():
  global buff
  global strip
  if len(buff) == 0:
    return
  if isMac():
    if debug: print buff
  else:
      for v in buff:
        strip.setPixelColor(v['pos'], v['color'])
      strip.show()
  buff = []
  
  

  
