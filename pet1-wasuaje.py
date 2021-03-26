import sys
n = int(input())
c=[0,0,0,0]
X=" x "
V="^"
s=`n`
while n > 1 :
	h=0
	j=-1
	s  = ''
	for i in [2,3,5,7]:
		j+=1
		if n%i  == 0:
			h+=1
			n/=i
			c[j]+=1				
		A=c[j]
		if A>0 :
			if A==1:
				s+=`i`
			else:
				s+=`i`+V+`A`
			s+=X			
	if  h==0:	
		break

if n > 1:
	s+=`n`
k=len(s)		
if s[k-3:k]==X:
	s=s[0:k-3]
print s

