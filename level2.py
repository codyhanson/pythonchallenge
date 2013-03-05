#! /usr/bin/env python
#python challenge, level 2!

import re
import urllib2

url = 'http://www.pythonchallenge.com/pc/def/ocr.html'

#pull down the webpage
openedUrl = urllib2.urlopen(url)
page = openedUrl.read()

#extract the jumble from the page
matchJunk = re.compile("<!--(.*?)-->\s+$",re.MULTILINE|re.DOTALL)
junk = re.(matchJunk,page)
if (junk == None):
    print "didn't match"
else:
    print junk.group(1)

#match one character
pattern = re.compile(r"[a-z]") 

#one way to do it
output = ''
for char in page:
   m = re.search(pattern,char) 
   if (m != None):
       output = output + m.group(0)

#another way
m2 = re.findall(pattern,junk.group(1))

print ''.join(m2)

#looks like the last word is 'equality'
