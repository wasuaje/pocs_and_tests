#!/usr/bin/python

#dure 2:43seg
#f = open("pruebalog.log","r")

#for i in f:
# print i.split(" ")[0]


import fileinput
for line in fileinput.input("pruebalog.log"):
    print line.split(" ")[0]
