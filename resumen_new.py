#! /usr/bin/env python
#
# Script para obtener un resumen de la plataforma de tipo semaforo sin detalles
# Elaborado por W.A. - 17/12/2012
#

#Los imports necesarios
import os
import time
import sys
import subprocess
import commands

#Diccionario con direcciones de correo
dirs={}
dirs["sysadmin"]="wasuaje@eluniversal.com"
#dirs["sysadmin2"]="wasuaje@hotmail.com"

#Diccionario con los servidores
servers={}

servers["A-MWeb01"]={"ip":"204.228.236.6", "data":{}}
servers["A-MWeb02"]={"ip":"204.228.236.13", "data":{}}
servers["A-MWeb03"]={"ip":"204.228.236.17", "data":{}}
servers["A-MApp01"]={"ip":"204.228.236.2", "data":{}}
servers["A-MApp02"]={"ip":"204.228.236.7", "data":{}}
servers["A-mand10"]={"ip":"204.228.236.10", "data":{}}
#Servidores de la plataforma local
servers["B-wtes02"]={"ip":"10.3.1.2", "data":{}}
#servers["B-des239"]={"ip":"10.3.0.239", "data":{}}
servers["B-desa01"]={"ip":"10.3.1.3", "data":{}}
servers["B-prloca"]={"ip":"10.3.0.130", "data":{}}
servers["B-desa02"]={"ip":"10.2.60.60", "data":{}}
servers["B-unive3"]={"ip":"10.6.0.43", "data":{}}

titulos=[" / ", "ERR",  "WRN",  "PNC", "SEC", "OLDR",  "BIGRT", 
	 		 "OLDMA", "BIGM", "OLDC", "BIGC", "PRHR", "PRHM", "PRHC"]

#print servers["A-Web01"]["data"]
def run_cmd(comando):
	out = commands.getoutput(comando)
	return out  # This is the stdout from the shell command

def write_file(newLine):
	file = open("resumen2.txt", "w")
	file.write(newLine)
	file.close()

def sortedDictValues2(adict):
    keys = adict.keys()
    keys.sort()
    return keys

def send_mail():
	import smtplib
	# Import the email modules we'll need
	from email import MIMEText
	# Open a plain text file for reading.  For this example, assume that
	# the text file contains only ASCII characters.
	fp = open("resumen2.txt", 'rb')
	# Create a text/plain message
	msg = MIMEText.MIMEText(fp.read())
	fp.close()

	for mail in dirs.keys():
		msg['Subject'] = "Resumen de la plataforma"
		msg['From'] = "Sysadmin@eluniversal.com"
		msg['To'] = dirs[mail]
		prueba = dirs[mail]
		# Send the message via our own SMTP server, but don't include the envelope header.
		s = smtplib.SMTP('localhost')		
		s.sendmail(msg['From'], msg['To'],  msg.as_string())
		s.quit()

cmd_comms={"raiz":"df -ah | egrep \/$ | awk '{print $(NF-1)}' | sed 's/%//g' | head -1", 						
						"error":"cat /var/log/messages | grep error | tail | wc -l", 
						"warn":"cat /var/log/messages | grep warning | tail | wc -l", 
						"panic":"cat /var/log/messages | grep panic | tail | wc -l", 
						"secure":"tail -300  /var/log/secure | grep failure | wc -l", 
						"oldroot":"find /root -type f -maxdepth 2 -mtime +360 | grep -v '/\.' |wc -l", 
						"oldmand":"find /home/manduca -type f -maxdepth 2 -mtime +360 | grep -v '/\.' |wc -l", 
						"oldcrons":"find /home/crons -type f  -maxdepth 2 -mtime +360 | grep -v '/\.' |wc -l", 
						"bigroot":"find /root -type f -maxdepth 2 -size +50000k | wc -l", 
						"bigmand":"find /home/manduca -type f -maxdepth 2 -size +50000k | wc -l", 
						"bigcrons":"find /home/crons -type f  -maxdepth 2 -size +50000k | wc -l", 
						"prohiroo":"find /root -type f  | egrep '.mp3$|.mp4$|.jpg$|.mov$|.avi$|.gif$' | wc -l", 
						"prohiman":"find /home/manduca -type f  | egrep '.mp3$|.mp4$|.jpg$|.mov$|.avi$|.gif$' | wc -l", 
						"prohicro":"find /home/crons -type f  | egrep '.mp3$|.mp4$|.jpg$|.mov$|.avi$|.gif$' | wc -l",
						}

#Inicio recoleccion de data
#recorro servers

for srv in sortedDictValues2(servers):
	#recorro comandos
	for cmd in cmd_comms:
		error=0
		#print "Servidor: %s- Comando: %s  - Linea: ssh root@"% (srv, cmd)+servers[srv]['ip']+' '+cmd_comms[cmd]
		try:
			#ejecuto el comando para el servidor respectivo
			rrst=int(run_cmd("ssh root@"+ servers[srv]["ip"]+" "+cmd_comms[cmd]))			
		except:
			#print "Unexpected error:", sys.exc_info()[0]
			rst="N/A"
		else:
			rst=rrst
		#dentro de dir de servidores en el key data guardo el diccionario de resultados con keys:valo
		#print rst
		servers[srv]["data"][cmd]=rst
	#print servers[srv]["data"]
#cmd=int(run_cmd("ssh root@"+ servers["B-desa02"]["ip"]+" "+cmd_comms["raiz"]))
#print cmd, type(cmd)

#imprimo resultados
linea=""
rpt_head1="\t\t\t\tGerencia de Infraestructura de Sistemas\n"
rpt_head2="\t\t\t\t\tResumen de la plataforma\n"
rpt_head3="\t\t\t\t=======================================\n\n"

linea+=rpt_head1+rpt_head2+rpt_head3

linea+="Server\t\t"
for ln in titulos:
	linea+=str(ln)+"\t"

linea+="\n"
linea+="=================================================================================================================================\n\n"

for srv1 in sortedDictValues2(servers):
	for k in servers[srv1]["data"].keys():
		if  k in ('error', 'warn', 'panic', 'secure') and servers[srv1]["data"][k]==0:
			servers[srv1]["data"][k]="OK"
		elif  k in ('error', 'warn', 'panic', 'secure') and servers[srv1]["data"][k]>0:
			servers[srv1]["data"][k]="WARN"
		if k in ('raiz') and servers[srv1]["data"][k]<80 :
			servers[srv1]["data"][k]="OK"
		elif k in ('raiz') and servers[srv1]["data"][k]>=80 and servers[srv1]["data"][k]<=90:
			servers[srv1]["data"][k]="WARN"
		elif k in ('raiz') and servers[srv1]["data"][k]>90 :
			servers[srv1]["data"][k]="CRIT."
		if  k in ('oldroot', 'bigroot', 'oldmand', 'bigmand', 'oldcrons', 'bigcrons') and servers[srv1]["data"][k]==0:
			servers[srv1]["data"][k]="OK"	
		elif  k in ('oldroot', 'bigroot', 'oldmand', 'bigmand', 'oldcrons', 'bigcrons') and servers[srv1]["data"][k]=="N/A":
			servers[srv1]["data"][k]="N/A"
		elif  k in ('oldroot', 'bigroot', 'oldmand', 'bigmand', 'oldcrons', 'bigcrons') and servers[srv1]["data"][k]>=1 and servers[srv1]["data"][k]<50:
			servers[srv1]["data"][k]="WARN"	
		elif  k in ('oldroot', 'bigroot', 'oldmand', 'bigmand', 'oldcrons', 'bigcrons') and servers[srv1]["data"][k]>50:
			servers[srv1]["data"][k]="CRIT."	
		if  k in ('prohiroo', 'prohiman', 'prohicro') and servers[srv1]["data"][k]==0:
			servers[srv1]["data"][k]="OK"	
		elif  k in ('prohiroo', 'prohiman', 'prohicro') and servers[srv1]["data"][k]=="N/A":
			servers[srv1]["data"][k]="N/A"
		elif  k in ('prohiroo', 'prohiman', 'prohicro') and servers[srv1]["data"][k]>=1 and servers[srv1]["data"][k]<50:
			servers[srv1]["data"][k]="WARN"	
		elif  k in ('prohiroo', 'prohiman', 'prohicro') and servers[srv1]["data"][k]>50:
			servers[srv1]["data"][k]="CRIT."	
		

for srv2 in sortedDictValues2(servers):
	linea+= srv2+"\t"+servers[srv2]["data"]["raiz"]+"\t"+servers[srv2]["data"]["error"]+"\t" \
				+servers[srv2]["data"]["warn"]+"\t"+ \
				servers[srv2]["data"]["panic"]+"\t"+ \
				servers[srv2]["data"]["secure"]+"\t"+ \
				servers[srv2]["data"]["oldroot"]+"\t"+ \
				servers[srv2]["data"]["bigroot"]+"\t"+ \
				servers[srv2]["data"]["oldmand"]+"\t"+ \
				servers[srv2]["data"]["bigmand"]+"\t"+ \
				servers[srv2]["data"]["oldcrons"]+"\t"+ \
				servers[srv2]["data"]["bigcrons"]+"\t"+ \
				servers[srv2]["data"]["prohiroo"]+"\t"+ \
				servers[srv2]["data"]["prohiman"]+"\t"+ \
				servers[srv2]["data"]["prohicro"]+"\n"

linea+="\n"
linea+="=================================================================================================================================\n\n"
linea+="Comandos Utilizados:\n"
for ln in cmd_comms.keys():
	linea+=ln+"\t\t"+cmd_comms[ln]+"\n"
	
#print linea
#servers[srv2]["data"]["oldmand"]
#escribo el reporte en el archivo de texto
write_file(linea+"\n")

send_mail()










