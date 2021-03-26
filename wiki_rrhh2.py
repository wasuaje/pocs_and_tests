#!/usr/bin/python
# -*- coding: utf-8 -*-

import mwclient

url='ghlo.eluniversal.com'
site = mwclient.Site(url, path = '/')


#No requiere login
#rs= site.raw_api('createaccount',name='testuser2',password='test123')
#rs2= site.raw_api('createaccount',name='testuser2',password='test123',token=rs['createaccount']['token'])
#rs2['createaccount']['result']


#cambiar usuarios de grupo requiere login por cada cambio de usuario
#lg=site.login('wasuaje','123456')
#rs= site.raw_api('query',list='users',ususers='testuser2',ustoken='userrights')
#print rs['query']['users'][0]['userrightstoken']
#
#rs2= site.raw_api('userrights',user='testuser2',add='bbdd',token=rs['query']['users'][0]['userrightstoken'])
#print rs2['userrights']['added']

g=open('newwikiusers.txt')
for i in g.readlines():	
	username=i.split('\t')[0]
	password=i.split('\t')[1]
	email=i.split('\t')[2]
	realname=i.split('\t')[3]
	grupos=i.split('\t')[4].replace('\n','')
	#print username,password,email,realname,grupos

	#procedo a crear las cuentas de usuario
	rs= site.raw_api('createaccount',name=username,password=password,email=email,realname=realname)
	rs2= site.raw_api('createaccount',name=username,password=password,email=email,realname=realname,token=rs['createaccount']['token'])	
	
	#inmediatamente los asigno a sus grupos respectivos(deben estar creados antes por la aplicacion wiki)
	#primero hay que loguears
	lg=site.login('wasuaje','www4214')
	
	#ahora solicito el token que me autoriza a hacer el movimiento
	rs= site.raw_api('query',list='users',ususers=username,ustoken='userrights')
	print rs
	
	#ahora ejecuto en si la asignacion de grupos
	rs2= site.raw_api('userrights',user=username,add=grupos,token=rs['query']['users'][0]['userrightstoken'])
	print rs2
	#print username,password,email,realname,grupos

