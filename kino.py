# -*- coding: utf-8 -*-
import re
import random


TOT_NROS=15
NRO_IMPAR=9
#SUMA=range(185,210)
NRO_2CIF=9
NRO_CONS=9
NRO_SEPARA=2
LISTA_NROS=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
nros_ante=[]
sel_tot=0
corridas=0
while True:
	SUMA=random.randrange(190,210,1)
	corridas+=1
	selection=[]
	cont_cons=0
	have_first=0
	sel_tot=0
	#para elegir los 15 numero
	while len(selection) < 15:
		#primer numero al azar, lo repito hasta que sea menor que 17 para que no se pase de 25
		#y luego poder agregarle de una vez los consecutivos
		while have_first==0:
			first=random.randrange(1,25,1)
			if first<17:
				selection.append(first)
				sel_tot+=first
				have_first=1			
		#numero consecutivos a este
		while cont_cons < NRO_CONS:
			cont_cons+=1
			nb=first+cont_cons
			if nb not in  selection:
				selection.append(nb)
				sel_tot+=nb
		if len(selection) < 16:
			nb=nb+NRO_SEPARA
			if nb > 25:
				nb=random.randrange(1,25,1)
			if nb not in selection:
				selection.append(nb)
				sel_tot+=nb
	#pruebo determinando la suma random entre los mejores valores
	if (sel_tot+10 > SUMA or sel_tot-10 < SUMA)  and len(selection) >= 15 :
		impares=0
		for h in selection:
			if h%2 == 1:
				impares+=1
		if impares >= NRO_IMPAR:
			break
	print "valor a buscar",SUMA
	print "Corridas",corridas
	print "valor obtenido",sel_tot

print "total Corridas",corridas
print "seleccion final",sorted(selection)
print "tamaño de la selecccion ",len(selection)		
print "suma de la seleccion",sel_tot
		

			

