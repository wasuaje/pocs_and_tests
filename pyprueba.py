#! /usr/bin/env python
#Script tipo daemon para mantener vigilado una lista de directorio que 
#se lean desde un archivo de configuracion y se ejecutan las acciones especificadas
#Creado por Wuelfhis Asuaje a solicitud de ElUniversal

import subprocess
import optparse
import re
import os
import time
import sys
from daemon3x import Daemon

#archivo con la lista de directorios y acciones
CONFFILE='/etc/check_eu4.conf'
#copia del anterior pero con la fecha y hora agregada para comparar
TEMPFILE='/tmp/check_eu4.tmp'
data={}			#coloco en blanco el diccionario para adicionarle registros luego

#lleno una lista con los valores de los arhcivos 
def configread():
		#Abrimos ambos arh 
	conff = open(CONFFILE, 'r+')
	tempf = open(TEMPFILE, 'r+')
	for line in conff:
		sub=line.split(";")
		#data={sub[0]:[sub[1],file_date]}
		file_date=gettime(sub[0])
		data[sub[0]]=[sub[1],file_date]		
	#print data
	#print data["prueba2.txt"]
	conff.close()
	tempf.close()
	return data

def gettime(filepath):
	stats = os.stat(filepath)
	#
	# create tuple (year yyyy, month(1-12), day(1-31), hour(0-23), minute(0-59), second(0-59),
	# weekday(0-6, 0 is monday), Julian day(1-366), daylight flag(-1,0 or 1)) from seconds since epoch
	# note: this tuple can be sorted properly by date and time
	#
	lastmod_date = time.localtime(stats[8])
	file_date = time.strftime("%d/%m/%y %H:%M:%S", lastmod_date)
	return file_date

def timecheck():
	#"print "entra"
	cont=0
	for claves in data: 	  	
		linea=data[claves]		#obtengo la linea del diccionario que es una tupla accion,fecha
	  	TIME=linea[1]
	  	NEWTIME=gettime(claves)		#consulto directo al archivo por su nueva fecha y hora
		#print TIME,NEWTIME
	 	if TIME != NEWTIME:  		#si hay cambios en la fecha
	    		acmd=runcmd("sh "+linea[0])	#ejecute el comando establecido en caso que cambie ese archivo
			print acmd
			configread()				#leo el archivo de configuracion cuando haya cambios
			

def runcmd(comando):
	p = subprocess.Popen(comando, shell=True, stdout=subprocess.PIPE)
	out = p.stdout.read().strip()
	return out  #This is the stdout from the shell command



class MyDaemon(Daemon):
        def run(self):
		while [ 1 ]:                      
			time.sleep(1)
			timecheck()				# bucle infinito que compra fechas

if __name__ == "__main__":
        daemon = MyDaemon('/tmp/daemon-example.pid')
        if len(sys.argv) == 2:
                if 'start' == sys.argv[1]:
                        daemon.start()
			configread()				#leo el archivo de configuracion una vez 
                elif 'stop' == sys.argv[1]:
                        daemon.stop()
                elif 'restart' == sys.argv[1]:
                        daemon.restart()
			configread()				#leo el archivo de configuracion una vez 
                else:
                       print "Unknown command"
	               sys.exit(2)
	               sys.exit(0)

        else:

                print "usage: %s start|stop|restart" % sys.argv[0]

                sys.exit(2)






