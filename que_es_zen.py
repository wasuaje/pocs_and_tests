from fpdf import FPDF
import os
zendir="/home/wasuaje/Descargas/ElZenHabla/"
firstpage="1- El Zen Habla.jpg"

pdf=FPDF()
for i in range(1,161):
	x = 0
	y = 0
	if i==1:
		name=zendir+firstpage
	else:
		name=zendir+str(i)+".jpg"
	print name
	if os.path.exists(name):
		pdf.add_page()
		pdf.image(name,x,y,w=200,h=300,type='JPEG',link='')
	
pdf.output('tuto1.pdf','F')
