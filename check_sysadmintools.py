#! /usr/bin/env python
#
# plugin de Nagios para monitorear areas en especial de EU
# por ejemplos la cantidad de archivos grandes, o viejos,
# la existencia de archivos prohibidos jpg,mov,wav,mp3 etc
# recibe como parametro1: HOST, parametro 2:comando
# Elaborado por W.A. - 20/12/2012
# Para python <2.7 requiere instalar python-setuptools y luego easy-install argparse

#Los imports necesarios
import os
import time
import sys
import subprocess
import commands

#Los posibles valores de salida
EXITOK=0
EXITWA=1
EXITCR=2
EXITUK=-1

#Diccionario para almacenar el servidor y sus datos
servers={'ip':'', 'data':'', 'exit':0,'msg':''}

def run_cmd(comando):
	out = commands.getoutput(comando)
	return out  # This is the stdout from the shell command

cmd_comms={"raiz":"df -ah | egrep \/$ | awk '{print $(NF-1)}' | sed 's/%//g' | head -1", 						
						"error":"cat /var/log/messages | grep error | tail | wc -l", 
						"warn":"cat /var/log/messages | grep warning | tail | wc -l", 
						"panic":"cat /var/log/messages | grep panic | tail | wc -l", 
						"secure":"tail -300  /var/log/secure | grep failure | wc -l", 
						"oldroot":"find /root -type f -maxdepth 2 -mtime +360 | grep -v '/\.' |wc -l", 
						"bigroot":"find /root -type f -maxdepth 2 -size +50000k | wc -l", 
						"prohiroot":"find /root -type f  | egrep '.mp3$|.mp4$|.jpg$|.mov$|.avi$|.gif$|.wav$|.doc$|.pdf$' | wc -l", 
						"oldhome":"find /home -type f -maxdepth 2 -mtime +360 | grep -v '/\.' |wc -l", 												
						"bighome":"find /home -type f -maxdepth 2 -size +50000k | wc -l", 						
						"prohihome":"find /home -type f  | egrep '.mp3$|.mp4$|.jpg$|.mov$|.avi$|.gif$|.wav$|.doc$|.pdf$' | wc -l", 					
						"numconx":"netstat -ntu|wc -l", 
						}
						
def main (host, cmd, war=10, crit=50):
	try:
			#ejecuto el comando para el servidor respectivo
		rrst=int(run_cmd("ssh root@"+ host+" "+cmd_comms[cmd]))			
	except:
			#si da un excpecion aqui es que el comando no es valido para ese host
		rst="N/A"
	else:
		rst=rrst 
			#dentro de dir de servidores en el key data guardo el diccionario de resultados con keys:valo
			#print rst
	servers['ip']=host	
	servers["data"]=rst
	
	#Procesamiento del resultado obtenido por el ssh, guardar sys.exit y mensaje de salido para NAgios
	k=cmd

	if  k in ('error', 'warn', 'secure', 'panic') and servers["data"]==0:
		servers["msg"]="OK - 0 Events Found"
		servers["exit"]=EXITOK
	
	elif  k in ('error', 'warn' 'secure', 'panic') and servers["data"]>0 and servers["data"]<war:
		servers["msg"]="WARNING %s Events Found" % servers["data"]
		servers["exit"]=EXITWA
	
	elif  k in ('error', 'warn' 'secure', 'panic') and servers["data"]>=crit:
		servers["msg"]="CRITICAL %s Events Found" % servers["data"]
		servers["exit"]=EXITCR	
	
	if  k in ('oldroot', 'bigroot', 'oldhome', 'bighome') and servers["data"]==0:
		servers["msg"]="OK - 0 Files Found"
		servers["exit"]=EXITOK
	
	elif  k in ('oldroot', 'bigroot', 'oldhome', 'bighome') and servers["data"]=="N/A":
		servers["msg"]="Unknown - Command not valid for this host"
		servers["exit"]=EXITUK
	
	elif  k in ('oldroot', 'bigroot', 'oldhome', 'bighome') and servers["data"]>0 and servers["data"]<war:
		servers["msg"]="WARNING %s Files Found" % servers["data"]
		servers["exit"]=EXITWA
	
	elif  k in ('oldroot', 'bigroot', 'oldhome', 'bighome') and servers["data"]>=crit:
		servers["msg"]="CRITICAL %s Files Found there are too many" % servers["data"]
		servers["exit"]=EXITCR
	
	if  k in ('prohiroot', 'prohihome') and servers["data"]==0:
		servers["msg"]="OK - 0 Files Found"
		servers["exit"]=EXITOK
	
	elif  k in ('prohiroot', 'prohihome') and servers["data"]=="N/A":
		servers["msg"]="Unknown - Command not valid for this host"
		servers["exit"]=EXITUK

	elif  k in ('prohiroot', 'prohihome') and servers["data"]>0 and servers["data"]<war:
		servers["msg"]="WARNING %s Files Found" % servers["data"]
		servers["exit"]=EXITWA

	elif  k in ('prohiroot', 'prohihome') and servers["data"]>=crit:
		servers["msg"]="CRITICAL %s Files Found there are too many" % servers["data"]
		servers["exit"]=EXITCR

# Solo para probar el plugin, estos valores deben venir como parametro
#	if  k in ('numconx'):
#		war=12000
#		crit=20000
	if  k in ('numconx') and servers["data"]<war:
		servers["msg"]="OK - %s Connections" % servers["data"]
		servers["exit"]=EXITOK

	elif  k in ('numconx') and servers["data"]>=war and servers["data"]<crit:
		servers["msg"]="WARNING %s Connections" % servers["data"]
		servers["exit"]=EXITWA

	elif  k in ('numconx') and servers["data"]>=crit:
		servers["msg"]="CRITICAL %s Connections" % servers["data"]
		servers["exit"]=EXITCR
		
	return servers
#
import argparse
if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-H', '--host',  required=True)
	parser.add_argument('-n', '--command',  required=True)
	parser.add_argument('-w', '--warning' ,type=int )
	parser.add_argument('-c', '--critical' , type=int)
	parser.add_argument('-v', dest='verbose', action='store_true') # hace q al usar -v, verbose=True
	args = parser.parse_args()	
	#Ejecuto el main de este archivo con los parametros recogidos	
	main(args.host, args.command,  args.warning, args.critical)
	#imprimo el mensaje devuelto por main y salgo con el sys.exit guadado tambien
	print servers["msg"]
	sys.exit(servers["exit"])
