#! /usr/bin/env python
#python challenge, level 5

import re
import urllib2
import pickle
import pprint
import sys


#pronounce it: 'peak hell'. 
#picture is 'green hill'?
#Pickle!
url = 'http://www.pythonchallenge.com/pc/def/peak.html'
urlBanner = 'http://www.pythonchallenge.com/pc/def/banner.p'

urlBannerHdl = urllib2.urlopen(urlBanner)
banner = urlBannerHdl.read()

#unpickle the banner.p file
bannerobj = pickle.loads(banner)

#my hypothesis is that the ' ' and the '#' make some kind of ascii art.
#when printed in the proper way
for item in bannerobj:
    for subitem in item:
        sys.stdout.write(subitem[0] * subitem[1])
    sys.stdout.write('\n')

#POST MORTEM: That was sweet as hell.
#output stored in level5-output.txt
