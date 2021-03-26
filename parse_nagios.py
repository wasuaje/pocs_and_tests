#! /usr/bin/env python
#
#Script para obtener un resumen de la plataforma
#Elaborado por W.A. - 14/01/2014

#Los imports necesarios
import re
import subprocess
#from pymongo import MongoClient
from pymongo import Connection
import datetime

def parseConf(source):
	conf = []
	for line in source.splitlines():
	    line=line.strip()
	    matchID = re.match(r"(?:\s*define)?\s*(\w+)\s+{", line)
	    matchAttr = re.match(r"\s*(\w+)(?:=|\s+)(.*)", line)
	    matchEndID = re.match(r"\s*}", line)
	    if len(line) == 0 or line[0]=='#':
	        pass
	    elif matchID:
	        identifier = matchID.group(1)
	        cur = [identifier, {}]
	    elif matchAttr:
	        attribute = matchAttr.group(1)
	        value = matchAttr.group(2).strip()
	        cur[1][attribute] = value
	    elif matchEndID and cur:
	        conf.append(cur)
	        del cur
	return conf

if __name__ == "__main__":
	#me traigo el archivo de nagios desde su ubicacion
	comando='scp root@m130:/usr/local/nagios/var/status.dat .'
	p = subprocess.Popen(comando, shell=True, stdout=subprocess.PIPE)
	
	#abro el archivo y lo dejo como string
	fl=open("status.dat")
	pl=fl.read()
	#print pl
	
	#recorro la data para obtener lo que necesito
	info = parseConf(pl)
	
	#abro la conexio a la bbd mongo que debe estar arriba para que esto funcione	
	connection = Connection('localhost', 3002)	
	db = connection.meteor
	db.services.drop()
	collection = db.services
	for k in info:
		#print k
		#if 'hoststatus' in k[0]:
		#	print k[1]['host_name'],k[1]['current_state']
		if 'servicestatus' in k[0]:
			#print k[1]['host_name'],k[1]['service_description'],k[1]['current_state'],k[1]['plugin_output'],k[1]['next_check']
			stampa=int(k[1]['next_check'])			
			nextcheck=datetime.datetime.fromtimestamp(stampa)
			nextcheck=nextcheck.strftime('%H:%M:%S' )
			collection.insert({'host':k[1]['host_name'],
					   'service':k[1]['service_description'],
					   'servicestatus':k[1]['current_state'],
						'plugin_output':k[1]['plugin_output'],
						'next_check':nextcheck
					   })
