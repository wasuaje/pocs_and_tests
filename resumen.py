#! /usr/bin/env python
#
# Script para obtener un resumen de la plataforma
# Elaborado por W.A. - 31/05/2010
# Modificado por w.a. 17/12/2012

#Los imports necesarios
import os
import time
import sys
import subprocess
import commands


#Diccionario con direcciones de correo
dirs={}
dirs["sysadmin"]="wasuaje@eluniversal.com"
#dirs["sysadmin2"]="wasuaje@hotmail.com"

#Diccionario con los servidores
servers={}
#servers["A-manduca5"]="204.228.236.5"
servers["A-Web01"]="204.228.236.6"
#servers["A-manduca8"]="204.228.236.31"
servers["A-manduca10"]="204.228.236.10"
servers["A-Web02"]="204.228.236.13"
servers["A-Web03"]="204.228.236.17"
servers["A-App01"]="204.228.236.2"
servers["A-App02"]="204.228.236.7"
#Servidores de la plataforma local
servers["B-webtest02"]="10.3.1.2"
servers["B-239"]="10.3.0.239"
servers["B-desa01"]="10.3.1.3"
servers["B-prodlocal"]="10.3.0.130"
servers["B-desa02"]="10.2.60.60"
servers["B-universal3"]="10.6.0.43"



#Diccionario con comandos
cmds={}
cmds["df"]=["Espacio en disco disponible","df -ah"]
cmds["df2"]=["Espacio en disco disponible","df -ak"]
cmds["log1"]=["Estado de los logs Static","ls -lah /usr/local/nginx-statics/logs"]
cmds["log2"]=["Estado de los logs EU","ls -lah /usr/local/eu-dyn/logs"]
cmds["log3"]=["Estado de los logs Estampas","ls -lah /usr/local/es-dyn/logs"]
cmds["log4"]=["Estado de los logs CEU","ls -lah /usr/local/apache-ceu/logs"]
cmds["log5"]=["Estado de los logs Widgets","ls -lah /usr/local/apache-widgets/logs"]
cmds["log6"]=["Estado de los logs OpenAdstream","du -sh  /home/manduca/apache/htdocs/RealMedia/ads/OpenAd/Logs/*"]
cmds["log7"]=["Estado de la cola de correo","mailq | grep Total"]
cmds["log8"]=["Estado de los logs de Apache OAS","ls -lah /home/manduca/apache/logs/"]
cmds["log9"]=["Estado de la Tmp","find /tmp -name *.jpg"]
cmds["log10"]=["Estado de logs de jboss","ls -lah /usr/local/jboss/server/default/log"]
cmds["log11"]=["Estado de logs de Tomcat","ls -lah /opt/apache-tomcat-6.0.29/logs"]
cmds["log12"]=["Estado de logs de Nginx","ls -lah /usr/local/nginx/logs"]
cmds["warn"]=["Warns del sistema operativo","cat /var/log/messages | grep warning"]
cmds["error"]=["Errors del sistema operativo","cat /var/log/messages | grep error | tail"]
cmds["panic"]=["Panics del sistema operativo","cat /var/log/messages | grep panic | tail"]
cmds["secure"]=["Alertas de seguridad de acceso","tail -300  /var/log/secure | grep failure"]
#cmds["crons"]=["Estado de las ultimas ejecuciones de los crons","tail -30 /var/log/cron"]
#cmds["crons1"]=["Listado de los cronjobs","\"find /var/spool/cron/ -type f -exec cat {} \; \""]
#cmds["crons2"]=["Listado de los cronjobs - Solaris","\"find /var/spool/cron/crontabs/ -type f -exec cat {} \; \""]
#cmds["crons3"]=["Listado de los cronjobs - Solaris - Manduca5","tail -30/var/cron/log"]
#cmds["crons4"]=["Estado de las ultimas ejecuciones de los crons","tail -30 /var/log/cron/info"]
cmds["check_dir1"]=["Monitoreo de Directorios LOG OAS","du -sh /home/manduca/apache/htdocs/RealMedia/ads/OpenAd/Logs/*"]
cmds["check_dir2"]=["Monitoreo de Directorios APP LOGS","du -sh /manduca10/applications/logs/*"]
cmds["check_dir3"]=["Monitoreo de Directorios OBM LOGS","du -sh /root/.obm/log/*"]
cmds["check_dir5"]=["Monitoreo de Directorio NGINX LOGS","ls -lah /usr/local/nginx/logs/*.log"]
cmds["check_dir6"]=["Monitoreo de Directorio NGINX LOGS","ls -lah /usr/local/nginx-lb/logs/*.log"]
cmds["check_dir7"]=["Monitoreo de Directorio NGINX LOGS","ls -lah /usr/local/nginx-statics/logs/*.log"]

cmds["check_homemanduca"]=["Monitoreo de Home Manduca","ls -lah /home/manduca"]
cmds["check_homecrons"]=["Monitoreo de Home Crons","ls -lah /home/crons"]
cmds["check_homeroot"]=["Monitoreo de Home Root","ls -lah /root"]

#este para app01 .2
cmds["check_dir4"]=["Monitoreo de Directorio MANDUCA LOGS","du -sh /manduca/logs/estampas/*"]

#para maquina solaris
cmds["warn1"]=["Warns del sistema operativo - Solaris","cat /var/log/syslog | grep warning"]
cmds["error1"]=["Errors del sistema operativo - Solaris","cat /var/log/syslog | grep error"]
cmds["panic1"]=["Panics del sistema operativo - Solaris","cat /var/log/syslog | grep panic"]
cmds["secure1"]=["Alertas de seguridad de acceso - Solaris","tail -300  /var/log/authlog | grep Failed"]

#Diccionario de comandos por servidor para evitar que servidores ejcuten comandos que no les correnponde
cmd_srv={}
cmd_srv["A-manduca5"]=[cmds["df2"],cmds["warn1"],cmds["error1"],cmds["panic1"],cmds["secure1"]]

cmd_srv["A-Web01"]=[cmds["df"],cmds["log1"],cmds["log2"],cmds["log4"],cmds["log5"],cmds["log11"],cmds["log12"],cmds["warn"],cmds["error"],cmds["panic"],cmds["secure"],cmds["check_dir5"],cmds["check_dir6"],cmds["check_dir7"],cmds["check_homemanduca"],cmds["check_homeroot"]]
cmd_srv["A-Web02"]=[cmds["df"],cmds["log1"],cmds["log2"],cmds["warn"],cmds["error"],cmds["panic"],cmds["secure"],cmds["check_homemanduca"],cmds["check_homeroot"]]
cmd_srv["A-Web03"]=[cmds["df"],cmds["log1"],cmds["log2"],cmds["warn"],cmds["error"],cmds["panic"],cmds["secure"],cmds["check_homemanduca"],cmds["check_homeroot"]]
cmd_srv["A-App01"]=[cmds["df"],cmds["log9"],cmds["log10"],cmds["warn"],cmds["error"],cmds["panic"],cmds["secure"],cmds["check_homemanduca"],cmds["check_homeroot"]]
cmd_srv["A-App02"]=[cmds["df"],cmds["warn"],cmds["error"],cmds["panic"],cmds["secure"],cmds["check_homemanduca"],cmds["check_homeroot"],cmds["check_homecrons"]]
cmd_srv["A-manduca10"]=[cmds["df"],cmds["log8"],cmds["log6"],cmds["log7"],cmds["warn"],cmds["error"],cmds["panic"],cmds["secure"],cmds["check_dir1"],cmds["check_dir2"],cmds["check_dir3"],cmds["check_dir5"]]
cmd_srv["B-webtest02"]=[cmds["df"],cmds["warn"],cmds["error"],cmds["panic"],cmds["secure"],cmds["check_homemanduca"],cmds["check_homeroot"],cmds["check_homecrons"]]
cmd_srv["B-239"]=[cmds["df2"],cmds["warn1"],cmds["error1"],cmds["panic1"],cmds["secure1"]]
cmd_srv["B-prodlocal"]=[cmds["df"],cmds["warn"],cmds["error"],cmds["panic"],cmds["secure"],cmds["check_homemanduca"],cmds["check_homeroot"],cmds["check_homecrons"]]
cmd_srv["B-desa02"]=[cmds["df"],cmds["warn"],cmds["error"],cmds["panic"],cmds["secure"],cmds["check_homemanduca"],cmds["check_homecrons"],cmds["check_homeroot"]]
cmd_srv["B-universal3"]=[cmds["df"],cmds["warn"],cmds["error"],cmds["panic"],cmds["secure"],cmds["check_homemanduca"],cmds["check_homecrons"],cmds["check_homeroot"]]
cmd_srv["B-desa01"]=[cmds["df"],cmds["warn"],cmds["error"],cmds["panic"],cmds["secure"],cmds["check_homemanduca"],cmds["check_homecrons"],cmds["check_homeroot"]]

#devuelve una lista ordenada de las claves del diccionario
def sortedDictValues2(adict):
    keys = adict.keys()
    keys.sort()
    return keys

#funcion que abre archivo de texto donde se va a reunir la informacion
def write_file(newLine):
	file = open("resumen.txt", "w")
	file.write(newLine)
	file.close()

def run_cmd(comando):
	#p = subprocess.Popen(comando, shell=True, stdout=subprocess.PIPE)
	#out = p.stdout.read().strip()
        # cambio sencillo el 24/02/2011 elimino las 2 lin anteriores por solo 1 la siguiente
	out = commands.getoutput(comando)
	return out  # This is the stdout from the shell command

def send_mail():
	import smtplib
	# Import the email modules we'll need
	from email import MIMEText
	# Open a plain text file for reading.  For this example, assume that
	# the text file contains only ASCII characters.
	fp = open("resumen.txt", 'rb')
	# Create a text/plain message
	msg = MIMEText.MIMEText(fp.read())
	fp.close()

	for mail in dirs.keys():
		msg['Subject'] = "Resumen diario de la plataforma"
		msg['From'] = "Sysadmin@eluniversal.com"
		msg['To'] = dirs[mail]
		prueba = dirs[mail]
		# Send the message via our own SMTP server, but don't include the envelope header.
		s = smtplib.SMTP('localhost')		
		s.sendmail(msg['From'], msg['To'],  msg.as_string())
		s.quit()

def begin_ser(srv):
	linea="\n********************* Servidor:"+srv+" *******************************************\n"
	return linea

def end_serv(srv):
	linea="\n**********************************************************************************\n"
	return linea

def gather_info(srv,cmd):
	comando = cmd
	from time import strftime
	ip=servers[srv]
	fecha=strftime("%Y-%m-%d %H:%M:%S")
	linea="----------------------------------------------------------------------------\n"
	linea=linea+fecha+ " -- Ejecutando:  "+comando[0] + "  --\n"
	linea=linea+"----------------------------------------------------------------------------\n"
	linea=linea+run_cmd("ssh root@"+ip+" "+comando[1])
	linea=linea+"\n"
	return linea

def main(server , comando ):
    linea=""
    if ',' in comando:
        comando = comando.split(',')
        #print comando
    if server == "" and comando == "":		#toda la corrida
		a=sortedDictValues2(servers)		#solicito la lista ordenada de claves
		for srv in a:
			linea=linea+begin_ser(srv)
			for cmd in cmd_srv[srv]:
				linea=linea+gather_info(srv,cmd)
			linea=linea+end_serv(srv)
    elif server != "" and comando != "" and type(comando).__name__ !='list':		#un servidor un comando
        try:
            if servers[server] and cmds[comando]:
                srv=server				
                linea=linea+begin_ser(srv)
                linea=linea+gather_info(srv,cmds[comando])
                linea=linea+end_serv(srv)
        except KeyError:
            linea="El servidor especificado o el comando no existe,los servidores y comandos validos son\n"            
            for srv in servers.keys():
				linea=linea+srv+"\n"				
            for cmd in cmds.keys():
				linea=linea+cmd+"\n"

    elif server != "" and comando == "":		#un servidor todos sus comandos
        srv=server	
        linea=linea+begin_ser(srv)
        for cmd in cmd_srv[srv]:
            linea=linea+gather_info(srv,cmd)
        linea=linea+end_serv(srv)
    
    elif server != "" and type(comando).__name__=='list': #un servidor varios comandos
        srv=server	
        linea=linea+begin_ser(srv)
        for cm in comando:            
            #print cm,srv
            linea=linea+gather_info(srv,cmds[cm])
        linea=linea+end_serv(srv)

    print linea
    write_file(linea+"\n")

if len(sys.argv) == 2:
	parametro=sys.argv[1]		
	parametro2=""
elif len(sys.argv) == 3:
	parametro=sys.argv[1]		
	parametro2=sys.argv[2]		
else:
	parametro=""
	parametro2=""

main(parametro,parametro2)

send_mail()
