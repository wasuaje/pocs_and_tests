import sys, random
success=0
theone= random.randint(1, 10000)
dif=random.randint(1, 20)
low=theone-dif
hig=theone+dif
sys.stdout.write(str(low))
sys.stdout.write(' ')
sys.stdout.write(str(hig))
sys.stdout.write('\n')
sys.stdout.flush()
#print theone
while success == 0:	
	val = random.randint(1, 10000)
	print val
	if val < theone:
		ans='LOW'
	elif val > theone:
		ans='HIGH'
	elif val == theone:
		ans='WIN'
		success=1
	sys.stdout.write(ans)
	sys.stdout.write('\n\n')
	sys.stdout.flush()
	
