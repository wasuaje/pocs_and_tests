#! /usr/bin/env python
#
#Script
#Elaborado por W.A. - 7/09/2010

#Los imports necesarios
import sys
cont=0
n=sys.stdin.readlines()
for i in n:
	cont=cont+int(i)
print cont

