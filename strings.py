#! /usr/bin/env python
#
#Script para 
#Elaborado por W.A. - 31/05/2010

#Los imports necesarios
import os
import time
import sys
import subprocess
import re

def open_file():
	file = open("resumen.txt", "r")
	archivo=file.read()
	file.close()
	return archivo
	
#a=open_file()
#print a
#pattern=re.compile('([8-9]?[0-9])%')
#m = pattern.match('81%') 

pattern=re.compile('[2000-2010]')
m = pattern.match('1999') 


if m == None:
	print "No hay datos\n"
else:
	print m.group()
