#Encuentra los palindromos 

top=10000000

for i in range(1,top):
	if str(i) == str(i)[::-1]:
		print str(i), '<- Palindromo'
