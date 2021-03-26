# -*- coding: IBM850 -*- 

#### -*- coding: utf-8 -*-
### required - do no delete

#Script para ayudar a la automatizacion de la creacion de carpeta mensual para interfaces de SAP
#Creado por Infraestructura de Sistemas el 30/05/2012


import subprocess
import optparse
import re
import os
import time
import sys
import datetime

#directorio de destino de los archivos

#produccion
#TARGETDIR='c:\\'

#para pruebas

#prueba = 'comienzo'
#print prueba
TARGETDIR = 'c:\\'
#print TARGETDIR
lista = ['jbarrera@eluniversal.com','wasuaje@eluniversal.com']
meses={1:'Enero',2:'Febrero', 3:'Marzo', 4:'Abril', 5:'Mayo', 6:'Junio', \
			7:'Julio', 8:'Agosto', 9:'Septiembre', 10:'Octubre',11:'Noviembre', 12:'Diciembre'}

def runcmd(comando):
	p = subprocess.Popen(comando, shell=True, stdout=subprocess.PIPE)
	out = p.stdout.read().strip()
	return out  #This is the stdout from the shell command

def send_mail(emaillist,subject,message):
        
	import smtplib
	# Import the email modules we'll need
	from email.mime.text import MIMEText
	msg = MIMEText(message)

	for mail in emaillist:
		msg['Subject'] = subject
		msg['From'] = "SysAdmin@eluniversal.com"
		msg['To'] = mail
		mailto = mail
		# Send the message via our own SMTP server, but don't include the envelope header.
		s = smtplib.SMTP('10.3.0.130')		
		s.sendmail(msg['From'], mailto, msg.as_string())
		s.quit()
		
#Obtener nro del mes actual
		
curdate= datetime.date.today()

curyear=curdate.year

curmonth=curdate.month

curmonthname=meses[curmonth]

if curmonth == 1:
	prevmonthname=meses[12]
	curyear=curdate.year-1
	curyear2=curdate.year
else:
	prevmonthname=meses[curmonth-1]
	
dirtocreate=curmonthname+"_"+str(curyear2)
dirtozip=prevmonthname+"_"+str(curyear)

#print 'dirtocreate = '+ dirtocreate
#print 'dirtozip = '+ dirtozip


#Si no existe el directorio lo creo
if not os.path.exists(TARGETDIR+dirtocreate):
    os.makedirs(TARGETDIR+dirtocreate)
    print 'Se creo el Directorio: '+ (TARGETDIR+dirtocreate)
else:
	print 'Directorio ya existe: '+ (TARGETDIR+dirtocreate)



#comprimir directorio anterior
import zipfile

zip_file = TARGETDIR+dirtozip

#print 'directorio para archivo zip ' + TARGETDIR+dirtozip

#zip = zipfile.ZipFile('/tmp/example.zip', 'w', zipfile.ZIP_DEFLATED)

#file_camino=TARGETDIR+dirtozip+chr(92)+ dirtozip+ '.zip'

file_camino=TARGETDIR+chr(92)+ dirtozip+ '.zip'

archivo = chr(92)+ dirtozip+ '.zip'


#print 'dirtozip : '+dirtozip
#print 'file_camino  '+file_camino
#print 'archivo : '+archivo

zip = zipfile.ZipFile(file_camino, 'w', zipfile.ZIP_DEFLATED)

rootlen = len(TARGETDIR+dirtozip) + 1
for base, dirs, files in os.walk(TARGETDIR+dirtozip):
   for file in files:
      fn = os.path.join(base, file)
      zip.write(fn, fn[rootlen:])
zip.close()

# se envia mensaje
subject = "creacion respaldo Interfases SAP al mes "+dirtozip


message = "Se realizo el proceso de respaldo de los archivos de interfases con exito correspondiente al mes de "+dirtozip


###send_mail(lista,subject,message)
send_mail(lista,subject,message)
