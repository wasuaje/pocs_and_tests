#!/bin/env python
# -*- coding: utf-8 -*-

import datetime
import os
import socket

#para
date=datetime.datetime.now()
data={}
data["deu-app-01"]=["/usr/local/apache-tomcat/logs","/manduca/logs/","/local2/applications/"]
data["deu-app-02"]=["/usr/local/jboss-5.1.0.GA/server/default/deploy/Applite/logs/",
                   "/usr/local/apache-tomcat/logs","/usr/local/elasticsearch-0.20.6/logs"]
data["deu-app-03"]=["/usr/local/apache-tomcat/logs","/usr/local/elasticsearch-0.20.6/logs"]
data["wasuaje-desktop"]=["/home/wasuaje/Documentos/desarrollo"]

listamails = ['azambrano@eluniversal.com','wasuaje@eluniversal.com']

hostname=socket.gethostname()
mensaje="Se procesaron exitosamente los siguientes logs:\n"
subject="Mantenimiento de logs en: %s" % hostname

def send_mail(emaillist,subject,message):

        import smtplib
        # Import the email modules we'll need
        from email.mime.text import MIMEText
        msg = MIMEText(message)

        for mail in emaillist:
                msg['Subject'] = subject
                msg['From'] = "infra-sistemas@eluniversal.com"
                msg['To'] = mail
                mailto = mail
                # Send the message via our own SMTP server, but don't include the envelope header.
                #s = smtplib.SMTP('10.3.0.130')#pruebas
                s = smtplib.SMTP('localhost')#produccion
                s.sendmail(msg['From'], mailto, msg.as_string())
                s.quit()

def main_proc(mensaje,subject):
	mensaje2=""
	for dr in data[hostname]:	
		for root, dirs, files in os.walk(dr):
			for fl in files:
				if fl.endswith('.log') or fl.endswith('.log.gz')  or fl.endswith('.gz') or '.log' in fl or ('log_' in fl and fl.endswith('.txt')):
					curpath = os.path.join(root, fl)
					file_modified = datetime.datetime.fromtimestamp(os.path.getmtime(curpath))				
					if datetime.datetime.now() - file_modified > datetime.timedelta(days=7):
						mensaje2+=curpath+"\n"
						#print curpath,file_modified ,datetime.datetime.now() - file_modified
	          			os.remove(curpath)
	if mensaje2=="":
		mensaje+="\n\nNo se encontraron logs que procesar hoy"
	else:
		mensaje+=mensaje2
	send_mail(listamails,subject,mensaje)


if __name__ == "__main__":
	main_proc(mensaje,subject)
