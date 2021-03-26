
import operator 

deudas={}
deudas['caja']=(852, 428)
deudas['extra']=(960, 320)
deudas['corp']=(2500, 150)
deudas['provin']=(2500, 160)

sorted_deudas = sorted(deudas.iteritems(), key=operator.itemgetter(1), reverse=False)
print sorted_deudas
pago=0
nsaldo=0
mes=0
for idx in range(len(sorted_deudas)):	
	saldo=sorted_deudas[idx][1][0]+nsaldo
	print sorted_deudas[idx][0],  '==' , saldo
	pago+=sorted_deudas[idx][1][1]
	while saldo > 0:
		mes+=1
		nsaldo=saldo-pago
		saldo=nsaldo
		print 'Mes:'+str(mes)+' '+str(saldo)+' - '+str(pago)
		
		
		
