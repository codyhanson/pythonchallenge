#! /usr/bin/env python
#python challenge, level 5

import re
import urllib2


#pronounce it: 'peak hell'. 
# font color: #c0c0ff. pronounce that too?
url = 'http://www.pythonchallenge.com/pc/def/peak.html'
urlBanner = 'http://www.pythonchallenge.com/pc/def/banner.p'

urlBannerHdl = urllib2.urlopen(urlBanner)
banner = urlBannerHdl.read()

#try to remove all the p's?
