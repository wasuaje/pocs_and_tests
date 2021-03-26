import shelve

animales = ["mamiferos", "peces", "insectos"]
insectos = ["grillo","cucaracha","chiripa"]
lenguajes = ["python", "mono", "perl"]

shelf = shelve.open("datos3.dat")

#Si cambio un valor en un dicc debo hacer un re-shelf

shelf["primera"] = animales
shelf["segunda"] = insectos
shelf["tercera"] = lenguajes

#print dir(shelf["segunda"])

for ins in shelf["tercera"]:
		print ins+":",
#		for isec in lenguajes:
#			print isec,
	 

shelf.close()
