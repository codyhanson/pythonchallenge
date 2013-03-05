#! /usr/bin/env python
#python challenge. Level 3!

import re
import urllib2

url = 'http://www.pythonchallenge.com/pc/def/equality.html'

#pull down the webpage
openedUrl = urllib2.urlopen(url)
page = openedUrl.read()

#extract the jumble from the page
matchJunk = re.compile("<!--(.*?)-->\s+$",re.DOTALL)
junk = re.search(matchJunk,page)

pattern = re.compile(r"(?:^|[a-z])[A-Z]{3}([a-z])[A-Z]{3}(?:[a-z]|$)",re.MULTILINE) 

m = re.findall(pattern,junk.group(1))

if (m == None):
    print "none found"
else:
    print ''.join(m)
