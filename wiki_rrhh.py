#!/usr/bin/python
# -*- coding: utf-8 -*-


import os
import subprocess
import urllib
import urllib2
import simplejson as json

url = 'http://ghlo.eluniversal.com/api.php'

def list_users():
	#format=json&action=query&list=allusers&aulimit=500&auprop=groups
	submitVars={}
	submitVars['format']='json'
	submitVars['action']='query'
	submitVars['list']='allusers'
	submitVars['aulimit']=500
	submitVars['auprop']='groups'

	#Lista usuarios del wiki
	submitVarsUrlencoded = urllib.urlencode(submitVars)
	req = urllib2.Request(url, submitVarsUrlencoded)
	response = urllib2.urlopen(req)
	thePage = response.read()
	f=json.loads(thePage)
	print f

def get_token():
	submitVars={}
	submitVars['format']='json'
	submitVars['action']='tokens'
	submitVars['type']='edit'
	submitVarsUrlencoded = urllib.urlencode(submitVars)
	req = urllib2.Request(url, submitVarsUrlencoded)
	response = urllib2.urlopen(req)
	thePage = response.read()
	f=json.loads(thePage)
	return f['tokens']['edittoken']

def createaccount(name,password,email,realname,token=''):
	submitVars={}	
	submitVars['format']='json'
	submitVars['action']='createaccount'
	submitVars['name']=name
	submitVars['password']=password	
	if token!= '':
		submitVars['token']=token
	submitVars['email']=email
	submitVars['realname']=realname	
	headers = {"Content-type": "application/x-www-form-urlencoded"}
	
	submitVarsUrlencoded = urllib.urlencode(submitVars)
	req = urllib2.Request(url, submitVarsUrlencoded, headers)	

	print submitVarsUrlencoded	

	response = urllib2.urlopen(req)	
	thePage = response.read()	
	f=json.loads(thePage)	
	print f
	if token != '' :		
		return f['createaccount']['result']		
	else:						
		return f['createaccount']['token']
	

def login(token='',sessionid=''):
	submitVars={}	
	submitVars['format']='json'
	submitVars['action']='login'
	submitVars['lgname']='wasuaje'
	submitVars['lgpassword']='123456'
	submitVars['lgtoken']=token
	#submitVars['sessionid']=sessionid
	if token != '' and sessionid != '':
		#(Set-Cookie: enwiki_session=17ab96bd8ffbe8ca58a78657a918558e; path=/; domain=.wikipedia.org; HttpOnly)
		headers = {"Set-Cookie":"sessionif=%s; path=/; domain=ghlo.eluniversal.com; " % sessionid,
				'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
	else:
		headers = {"Content-type": "application/x-www-form-urlencoded",
		'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
	
	submitVarsUrlencoded = urllib.urlencode(submitVars)
	req = urllib2.Request(url,submitVarsUrlencoded,headers)
	print req.header_items()
	response = urllib2.urlopen(req)
	thePage = response.read()
	f=json.loads(thePage)
	print f
	if token != '' and sessionid != '':		
		return f['login']['result']		
	else:						
		return f['login']['token'],f['login']['sessionid']
		

#print get_token()
token,sessionid=login()
print token,sessionid
login(token,sessionid)
#print token
#token= createaccount('prueba','prueba01','prueba01@prueba01.com','prueba 01')
#print token
#print createaccount('prueba','prueba01','prueba01@prueba01.com','prueba 01',token)
#print list_users()