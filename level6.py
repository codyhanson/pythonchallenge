#! /usr/bin/env python
#Python Challenge, Level 6

import urllib2
import pickle
import re
import string
import sys
import StringIO
from PIL import Image

url = 'http://www.pythonchallenge.com/pc/def/channel.html'
urlImg = 'http://www.pythonchallenge.com/pc/def/channel.jpg'

#hints: Channel, <-- zip (means unzip?), now there are pairs


urlImgHdl = urllib2.urlopen(urlImg)
imageData = urlImgHdl.read()

pairs = zip(*[imageData]*2)

bands = zip(*pairs)
print bands

img = Image.merge("LA",bands)

img.save("img.jpg")

#turn bytes into hex string
#imageHex = ":".join("{0:x}".format(ord(c)) for c in imageData)
imageHex = "".join("{0:x}".format(ord(c)) for c in imageData)

#print imageHex

for i in xrange(len(imageHex)):
    if imageHex[i:i+4] == 'fffe':
        pass
    #print imageHex[i:i+60].decode("hex")



#sfp = StringIO.StringIO(imageData)
#im = Image.open(sfp)

#print im

#z1,z2,z3 = zip(*imageData)

