#! /usr/bin/env python
#
#Script para 
#Elaborado por W.A. - 31/05/2010

#Los imports necesarios


from traceback import format_exc
#import shelve
import  anydbm

animales = ["piton", "mono", "camello"]  
lenguajes = ["python", "mono", "perl"]  

a = anydbm.open("datos.dat","c")


a["primera"] = '1'
a["primera"] = '11'
a["primera"] = '111'
a["segunda"] = '2' 
a["tercera"] = '3'

print a


a.close()
