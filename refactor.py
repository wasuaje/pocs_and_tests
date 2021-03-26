import sys
n = int(sys.argv[1])
v=[2,3,5,7]
c=[0,0,0,0]
X=" x "
while True :
	h=0
	for i in range(len(v)):
		if n%v[i]  == 0:
			h+=1
			n=n/v[i]
			c[i]+=1			
	if h == 0:
		break
s  = ''
for z in range(len(c)):
	if  c[z]<>0:	
		s+=str(v[z])+"^"+str(c[z])+X
if n > 1:
	s+=str(n)
k=len(s)	
if s[k-3:k]==X:
	s=s[0:k-3]

s=s.replace("^1","")	
print s
	

