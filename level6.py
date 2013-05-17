#! /usr/bin/env python
#Python Challenge, Level 6

import urllib2
import re
import string
import sys
import zipfile

#hints: Channel, <-- zip (means unzip?), now there are pairs
url = 'http://www.pythonchallenge.com/pc/def/channel.html'
urlImg = 'http://www.pythonchallenge.com/pc/def/channel.jpg'

#disclaimer: I found online that this file existed. I was going the wrong direction.
#I thought that 'zip' was referring to the zip function. I was doing crazy image processing things
#on the channel.jpg
urlZip = 'http://www.pythonchallenge.com/pc/def/channel.zip'

urlZipHdl = urllib2.urlopen(urlZip)
channelzip = urlZipHdl.read()

zipFp = open('tmp/6/channel.zip', 'w')
zipFp.write(channelzip)
zipFp.close()

z = zipfile.ZipFile('tmp/6/channel.zip','r')

zhdl = z.open('readme.txt')

print zhdl.read()

#from readme.txt in channel.zip
#welcome to my zipped list.
#hint1: start from 90052
#hint2: answer is inside the zip

nothing = '90052'
nothingre = re.compile('(\d+)')

loop = True
while loop:
    fname = nothing + '.txt'
    zhdl = z.open(fname)
    txt = zhdl.read()
    m = re.search(nothingre,txt)
    if (m is None):
        print txt 
        loop = False
    else:
        nothing = m.group(1)

#after following the nothings, we get the message "collect the comments"
#I think this means collect the comments in the channel.jpg file

