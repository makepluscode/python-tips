#!/usr/bin/python

import datetime

nsec = datetime.datetime.now().second
s = str(nsec)
print (s + " sec")

s = ("%d" % (nsec))
print (s + " sec")
