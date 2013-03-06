#! /usr/bin/env python
#python challenge, level 4!

import re
import urllib2

baseurl = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'

nothingNumber = re.compile(r"(\d+)$")

url = baseurl + '?nothing=8022'

nothingsSeen = {}

#follow the ?nothing 's
for i in xrange(400):
    openedUrl = urllib2.urlopen(url)
    page = openedUrl.read()
    m = re.search(nothingNumber,page)
    if (m == None):
        print page
        break

    nothingNum = m.group(1)

    if (nothingNum in nothingsSeen):
        print "Seen {0} before".format(nothingNum)
    else:
        print i,nothingNum
        
    nothingsSeen[nothingNum] = True
    #next url
    url = baseurl + '?nothing=' + nothingNum 

