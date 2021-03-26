#! /usr/bin/env python
#
#Script
#Elaborado por W.A. - 7/09/2010

#Los imports necesarios
import sys

n=raw_input()
n=n.split(' ')
a=int(n[0])
b=int(n[1])
h=1
if b<a:
	a=b
	b=a

if a >= 1 and b<=10000:
	if b%a == 0:
		h=a
	else:
		h=b%a
	
else:
	sys.exit

if b==0 or a==0:
	h=0
print h

