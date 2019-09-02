# !/usr/bin/python

import os, sys

fd = os.open("hello.txt", os.O_RDWR)
buf = os.read(fd, 12)

print (type(buf))     # <class 'bytes'>
print (buf)           # b'Hello, World'       
print (buf[0])        # 72 (is 'H' on ASCII CODE)

# Convert from bytes to str
buf_dec = buf.decode()
print (type(buf_dec)) # <class 'str'>
print (buf_dec)       # Hello, World

os.close(fd)
