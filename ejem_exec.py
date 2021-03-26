import datetime
#for i in range(5):
#    var='a'+str(i+1)
#    exec "%s=2*(i+1)" %var
#    exec "print %s" %var

# creando la tablas funciona perfecto
#for i in range(1,10):
#  var="def tabla_del_%s():\n\tfor j in range(1,10):\n\t\tprint str(i)+'*'+str(j)+'='+str(i*j) " %i
#  var1="tabla_del_%s()"%i
#  exec var
#  exec var1

def LL(tpldate):
  cntmon=0
  print type(tpldate)
  a = datetime.date(tpldate[0],tpldate[1],tpldate[2])
  if a.month in (1,3,5,7,8,10,12):
    maxd=31
  elif a.month in (4,6,9,11):
    maxd=30
  else:
    maxd=28

  for i in range (1,maxd+1):
    if datetime.date(2011,11,i).weekday()==0:
	cntmon+=1
  return cntmon

fecha="2011,11,15"
fecha=tuple(fecha.split(','))
fecha=tuple(int(s) for s in fecha)
print fecha

exec "print LL(fecha)" 
