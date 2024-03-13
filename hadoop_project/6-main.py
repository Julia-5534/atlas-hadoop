#!/usr/bin/python2.7


download = __import__('6-download').download


l = ["/holbies/input/lao.txt"]
download(l)
lao =  open("lao.txt", "r")
print(lao.read())
lao.close()
