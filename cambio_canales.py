# -*- coding: utf-8 -*-
#

import sys
import os


FILE='cambios_canales.csv'
f = open(FILE, 'r')
i=0
addresses = f.readlines()  

for address in addresses:	
    address=address.replace('\r\n','')
    #if email_address.match(address):
    if valid(address):
	pass
    else:
	print address
        write_file("'"+address+"';")
	i+=1

print i
