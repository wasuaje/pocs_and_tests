
maxnumber = 1000000000000
#for i in range(1,maxnumber):
i=0
while True:
	i+=1
	multi = 0
#	print i,
	for j in range(len(str(i))):
		multi += int(str(i)[j])**len(str(i))
#		print multi,
	if i == multi:
		print i, "es narcisista"

