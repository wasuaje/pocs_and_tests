#!/usr/bin/python
# -*- coding: utf-8 -*-
pregunta= """
5) ¿A quiénes aplica la Convención Colectiva? \n
Al personal definido en la convención colectiva, que regula las condiciones de trabajo existentes entre las partes. La información específica de los cargos puede ubicarse en cada convención. \n
Área: Relaciones Laborales \n
Tema: Negociación de convenciones \n
Empresa: Diario el Universal \n
Responsable: Gerencia de Relaciones Laborales y Sindicatos \n
Formato / Documentos / Leyes involucradas: Convención Colectiva de Trabajo \n
¿Dónde ubicarlo?: Gerencia de Relaciones Laborales \n
"""

import mwclient

url='ghlo.eluniversal.com'
site = mwclient.Site(url, path = '/')



#me logueo antes para tener usuario con que hacer los cambios
lg=site.login('wasuaje','www4214')
archivo='cargamasivawiki.csv'

file = open(archivo,'r')
for f in file:
	h=f.split('|')
	titulo=h[0]
	texto=h[1].replace('\\n','\n\n')	
	texto=texto.rstrip('')
	texto=texto.lstrip('')
	texto="<FONT FACE='arial' >"+texto+"</FONT>"
	#print "texto"+texto
	#obtengo el token para poder modificar la pregunta respectiva	
	rs1= site.raw_api('query',prop='info|revisions',intoken='edit',titles=titulo)	
	#separo el token obtenido del diccionario anterior para la edicion definitiva
	#print rs1
	#Atrapo error cuando este editando paginas existentes
	try:
		token = rs1['query']['pages']['-1']['edittoken']
	except KeyError:
		#print rs1
		# Asi busco bajo el numero de revision correspondiente el edittoken, si da error hago pass
		# es decir no interesa, ahora si no, asigno edittoken
		for i in rs1['query']['pages'].keys():
			try:			
				token=rs1['query']['pages'][i]['edittoken']		
			except KeyError:
				pass
	print token	

	#solicitud del cambio en si
	
	# de este modo ingreso texto nuevo
	#rs= site.raw_api('edit',title=titulo,section='new',text=texto,token=token)

	# de este modo edito el titulo existente, nolleva section !!!
	rs= site.raw_api('edit',title=titulo,text=texto,token=token)
