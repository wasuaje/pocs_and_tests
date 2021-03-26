# -*- coding: utf-8 -*-
import sys
#sys.path.append('/path/to/rrdtool/lib/python2.6/site-packages/')
import rrdtool
from rrdtool import update as rrd_update

import subprocess
import time

comandos=['apache_accesses',
		  'apache_processes',
		  'apache_volume',
		  'cpu',
		  ]			


def createdb():
 # in real life data_sources would be populated in loop or something similar
	data_sources=[
 				"DS:apache_accesses:DERIVE:120:U:U", 		 				
            	"RRA:AVERAGE:0.5:1:60", 
            	"RRA:MIN:0.5:1:60" ,
            	"RRA:MAX:0.5:1:60" 
 				]
	
	ts = int(time.time())

	rrdtool.create( 'apache_accesses.rrd', "--step", "60",
                 '--start', str(ts),
                 data_sources, 
                 )

def updatedb(value):	
	ret = rrd_update('apache_accesses.rrd', 'N:%s' %(value));	
	if ret:
 		print rrdtool.error()

def collectdata(data):
	comando='ssh root@m13 munin-run %s' % data
	p = subprocess.Popen(comando, shell=True, stdout=subprocess.PIPE)	
	res=p.stdout.read().replace('\n',' ').split(' ')
	#print res
	for i in range(len(res)):
		if i%2 == 1:
			#print res[i],ts
			updatedb(res[i])

def gengraph():	
	ret = rrdtool.graph( "apache.png", "--start", "-2h", "--vertical-label=Acces/s","--width", "800","--height","300", 
 "DEF:inoctets=apache_accesses.rrd:apache_accesses:AVERAGE", 
 "LINE:inoctets#00FF00:Accesos/Seg", 
 "COMMENT:\\n",
 "GPRINT:inoctets:AVERAGE:Avg Acces./Seg\: %6.2lf %S",
 "COMMENT:  ",
 "GPRINT:inoctets:MIN:Min Avg.Acces./Seg\: %6.2lf %S\\r", 
 "COMMENT:  ",
 "GPRINT:inoctets:MAX:Max Avg.Acces./Seg\: %6.2lf %S\\r", 
 "COMMENT: ",)


def ver():
	pass

#info = rrdtool.info('speed.rrd')
#for i in info:
	#print info[i],"\n"

#btener el timestamp para pasar
#1389177318
#createdb()

#print info['ds[speed].minimal_heartbeat']
def main (command):
	if command == 'collect':
		collectdata('apache_accesses')
	if command == 'graph':
		gengraph()
	if command == 'create':
		createdb()


import argparse
if __name__ == '__main__':
        parser = argparse.ArgumentParser()
        parser.add_argument('-c', '--command',  required=True)        
        parser.add_argument('-v', dest='verbose', action='store_true') # hace q al usar -v, verbose=True
        args = parser.parse_args()
        #Ejecuto el main de este archivo con los parametros recogidos   
        main(args.command)
        #imprimo el mensaje devuelto por main y salgo con el sys.exit guadado tambien
        






