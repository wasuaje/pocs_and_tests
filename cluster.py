#!/usr/bin/python
# -*- coding: utf-8 -*-


import commands
from optparse import OptionParser
import os
import datetime


class cluster:		
	def __init__(self ):
		self.basecmd="sudo crm resource %s %s %s"
	
	def control(self,recurso,operacion):
		comando=self.basecmd % (operacion,recurso,'')
		print self.run_cmd(comando)

	def migrate(self,recurso,operacion,nodo):
		comando=self.basecmd % (operacion,recurso,nodo)
		print self.run_cmd(comando)

	def status(self):
		comando="crm status"
		print self.run_cmd(comando)
		

	def cleanup(self,cleanup,recurso):
		comando=self.basecmd % (cleanup,recurso,'')
		print self.run_cmd(comando)

	def run_cmd(self,comando):
		#p = subprocess.Popen(comando, shell=True, stdout=subprocess.PIPE)
		#out = p.stdout.read().strip()
		# cambio sencillo el 24/02/2011 elimino las 2 lin anteriores por solo 1 la siguiente
		out = commands.getoutput(comando)
		return out  # This is the stdout from the shell command


if __name__ == "__main__":
	usage = " %prog [control|migrate|status|cleanup] recurso [nodo|start|stop]"
	parser = OptionParser(usage)
	#parser.add_option("-h", "--help", action="help")
		
	parser.add_option("-c", "--control",  action="store_true", dest="control", help='Control de recursos del Cluster')
	parser.add_option("-m", "--migrate",  action="store_true", dest="migrate", help='Migra recursos del cluster entre nodos')	
	parser.add_option("-s", "--status",  action="store_true", dest="status", help='Muestra el estado del cluster' )    	
	parser.add_option("-n", "--cleanup",  action="store_true", dest="cleanup", help='Limpia el failcount de un recurso del cluster' )    	
	parser.add_option("-r", "--recurso",  action="store", dest="recurso", help='El recursos a controlar o migrar' )    	
	parser.add_option("-d", "--destino",  action="store", dest="destino", help='El nodo de destino para migrar recursos' )    	
	parser.add_option("-o", "--operacion",  action="store", dest="operacion", help='Start | Stop | Restart' )    	

	(options, args) = parser.parse_args()

	cl=cluster()
	
	#print (options, args)
	if options.control:
		try:
			cl.control(options.recurso,options.operacion)
		except AttributeError:
			parser.print_help()

	elif options.migrate:
		try:
			cl.migrate(options.recurso,"migrate",options.destino)
		except AttributeError:
			parser.print_help()

	elif options.status:
		try:
			cl.status()
		except AttributeError:
			parser.print_help()

	elif options.cleanup:
		try:
			cl.cleanup("cleanup",options.recurso)
		except AttributeError:
			parser.print_help()