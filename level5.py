#! /usr/bin/env python
#python challenge, level 5

import re
import urllib2


#pronounce it: 'peak hell'. 
#picture is 'green hill'?
# font color: #c0c0ff. pronounce that too?
url = 'http://www.pythonchallenge.com/pc/def/peak.html'
urlBanner = 'http://www.pythonchallenge.com/pc/def/banner.p'

urlBannerHdl = urllib2.urlopen(urlBanner)
banner = urlBannerHdl.read()

output = ''
#try to remove all the p's?
for char in banner:
    if (char != 'p'):
        output = output + char

print output


#lines =  banner.split('\n')
#lines.sort()
#for line in lines:
#    print line
