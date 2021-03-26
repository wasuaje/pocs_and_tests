#!/usr/bin/python
import random

letters="abcdefghijklmnopqrsetuvwxyz"
symbols="!$%*-_|()"
minlen=8

password=""
pick = 1 	#para que comience siempre con una letra mayuscula

while len(password) <= minlen-1 :
	letnum=random.randint(1, len(letters)-1)	
	synnum=random.randint(1, len(symbols)-1)
	number=random.randint(0,9)
	
	if pick == 1 and password.find(letters[letnum].upper()) <= 0:
		nuevovalor = letters[letnum].upper()
	elif pick == 2 and password.find(letters[letnum]) <= 0:
		nuevovalor = letters[letnum]
	elif pick == 3 and password.find(symbols[synnum]) <= 0:
		nuevovalor = symbols[synnum]
	elif pick == 4 and password.find(str(number)) <= 0:
		nuevovalor = str(number)
	
	if len(password) > 2:
		if nuevovalor in letters and password[len(password)-1] in letters:
			exit	
		elif nuevovalor in symbols and password[len(password)-1] in symbols:
			exit
		elif nuevovalor in letters.upper() and password[len(password)-1] in letters.upper():
			exit
		else:
			password+=nuevovalor
        pick=random.randint(1,4)

print password

