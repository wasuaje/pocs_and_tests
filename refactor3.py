import sys
newnum = int(sys.argv[1])
newtext = ""
checker = 2                          

while checker*checker <= newnum:

	if newnum%checker == 0:
		newtext += `checker`
		newnum /=  checker       
		if newnum <> 1: 
			newtext += "."
	else:                   
		checker+=1       
if newnum <> 1:                                   
	newtext += `newnum`
     
#newtext=newtext.replace(".","^ x ")  
print newtext

f=newtext[0:1]
for i in newtext:
	if i=f:
		cn+=1
		s+=i
	else:
		cn=0
	print i
