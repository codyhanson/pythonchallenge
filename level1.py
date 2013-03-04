#!/usr/bin/env python
#http://www.pythonchallenge.com/pc/def/map.html

#K -> M
#O -> Q
#E -> G

from string import maketrans


stringdata = """ g fmnc wms bgblr rpylqjyrc gr zw fylb.
rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw 
fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. 
sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""

mappings = {}

def mapFunc(inCh):
    if (inCh in mappings):
        return mappings[inCh]
    else:
        return inCh

#it would seem that each letter needs to be
#shifted by two (mod 26?)
for i in xrange(26):
    mappings[chr(ord('a')+i)] =  chr(ord('a')+ ((i + 2) % 26))


print ''.join(map(mapFunc ,stringdata))

#apparently the preferred way is 'maketrans'
intab = mappings.keys()
intab = ''.join(intab)
outtab = ''
for key in intab:
    outtab = outtab + mappings[key]


translation = maketrans(intab,outtab)

print 'USING MAKETRANS'
print stringdata.translate(translation)

###############################################
#Part 2!
url = "http://www.pythonchallenge.com/pc/def/map.html"

print ''.join(map(mapFunc ,url))

T1 = url.translate(translation)
T2 = T1.translate(translation)
print T2
