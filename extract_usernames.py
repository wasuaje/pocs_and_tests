#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import shutil
import subprocess
import random
import string

from random import *

passwordGen = lambda length, badChars = '',alpha = '1234567890qwertyuiop[]asdfghjkl;zxcvbnm,.!@#$%^&*()_+-=-{}:<>|QWERTYUIOPASDFGHJKLZXCVBNM~`?': "".join([list(set(alpha)^set(badChars))[randint(0,len(list(set(alpha)^set(badChars)))-1)] for i in range(length)])


if os.path.exists('rrhh_usuarios_con_grupos.csv'):
	f=open('rrhh_usuarios_con_grupos.csv')
for i in f.readlines():
	#print i
	uname=i.split('\t')[1].split(',')[1].replace('\n','').replace(' ','')
	apel=i.split('\t')[1].split(',')[0].replace('\n','').replace('MOVIMIENTO DE ','').replace('EGRESO DE ','').split(' ')[0]
	groups=i.split('\t')[0].lower().replace('\n','')
	#print uname
	apel=apel.lower()
	fullname=i.split('\t')[1].replace('\n','').lower()
	uname=uname.replace('\n','').lower()
	passwordGen = lambda length, badChars = '',alpha = '1234567890qwertyuiop[]asdfghjkl;zxcvbnm,.!@#$%^&*()_+-=-{}:<>|QWERTYUIOPASDFGHJKLZXCVBNM~`?': "".join([list(set(alpha)^set(badChars))[randint(0,len(list(set(alpha)^set(badChars)))-1)] for i in range(length)])
	print uname[:1]+apel+'\t'+passwordGen(6,'!@#`[]$|?&%_+-=:;{}<>.()^,~')+'\t'+uname[:1]+apel+'@eluniversal.com'+'\t'+fullname+'\t'+groups
