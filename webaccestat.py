#!/usr/bin/fab -f
# -*- coding: utf-8 -*-
import os
import socket
import redis
from socket import gethostbyaddr
from fabric.api import *
dirs={}
dirs["sysadmin"]="wasuaje@eluniversal.com"
env.hosts = ['root@204.228.236.6', 'root@204.228.236.13', 'root@204.228.236.17']
env.keepalive=200
path='/usr/local/nginx/logs'
cmdredis='./redis-server  --dbfilename dump.rdb --save 60 1 &'
pathredis='/home/wasuaje/Documentos/desarrollo/redis-2.6.13/src'

#{
 #   'web': ['root@204.228.236.6', 'root@204.228.236.13', 'root@204.228.236.17'],
  #  'app': ['root@204.228.236.2', 'root@204.228.236.7']
#}

def run_cmd(comando):
	#p = subprocess.Popen(comando, shell=True, stdout=subprocess.PIPE)
	#out = p.stdout.read().strip()
	# cambio sencillo el 24/02/2011 elimino las 2 lin anteriores por solo 1 la siguiente
	out = commands.getoutput(comando)
	return out  # This is the stdout from the shell command

def redis_ready():	
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	result = s.connect_ex(('127.0.0.1', 6379))
	if(result == 0) :
		return True
	else:
		return False
	s.close()

def send_mail():
        import smtplib
        # Import the email modules we'll need
        from email import MIMEText
        # Open a plain text file for reading.  For this example, assume that
        # the text file contains only ASCII characters.
        fp = open("webaccesstat.txt", 'rb')
        # Create a text/plain message
        msg = MIMEText.MIMEText(fp.read())
        fp.close()

        for mail in dirs.keys():
                msg['Subject'] = "Resumen de Ip's con mas accesos"
                msg['From'] = "Sysadmin@eluniversal.com"
                msg['To'] = dirs[mail]
                prueba = dirs[mail]
                # Send the message via our own SMTP server, but don't include the envelope header.
                s = smtplib.SMTP('10.3.0.130')
                s.sendmail(msg['From'], msg['To'],  msg.as_string())
                s.quit()

def write_file(newLine):
        file = open("webaccesstat.txt", "a")
        file.write(newLine)
        file.close() 

def nslooky(ip):
      try:
           output = gethostbyaddr(ip)
           return output[0]
      except:
           output = "not found"
           return output

@parallel(pool_size=10)
def prepare_data():
	cmd="for i in $(ls /usr/local/nginx/logs/*.log.1); do cat $i | cut -d' ' -f1 >> ips.txt ; done"
	cmd11="cat ips.txt | sort|uniq -c|sort -rn| head -100 >> ip.txt "
	#cmd2="for i in $(ls /usr/local/nginx/logs/*.log.1); do cat $i | cut -d'\"' -f6 | sort >> ua.txt; done"
	cmd2="for i in $(ls /usr/local/nginx/logs/*.log.1); do head -700000 $i | cut -d'\"' -f6  >> uas.txt; done"
	cmd22="cat uas.txt | sort|uniq -c|sort -rn| head -100 | sed -e 's/ *//' -e 's/ /\t/' >> ua.txt "
	with cd(path):
		cmds = [	cmd, cmd11, cmd2, cmd22	]
		run(' && '.join(cmds))		

@parallel(pool_size=10)
def download_data():	
	get('/usr/local/nginx/logs/ip.txt', 'ip-%s.txt' % env.host )
	get('/usr/local/nginx/logs/ua.txt', 'ua-%s.txt' % env.host )
	

@hosts('root@204.228.236.6')
def process_data():
	if redis_ready():	
		r = redis.Redis("localhost", port=6379)		
	else:
		with lcd(pathredis):
			local(cmdredis)		
			r = redis.Redis("localhost", port=6379)			
	r.flushdb()	
	files_in_dir = os.listdir('./')
	for fl in files_in_dir:				
		if 'ip-root' in fl:	
			clave='ip'						
			input_file = open(fl, 'r')			
			for i in input_file:
				z=i.split('\n')[0].split(' ')
				z.reverse()				
				print 'clave: %s - IP: %s - VAL: %s' % (clave,  z[0], z[1])
				r.zincrby(clave, z[0], z[1] )
		elif 'ua-root' in fl:
			clave='ua'						
			input_file = open(fl, 'r')			
			for i in input_file:										
				z=i.split('\t')
				z.reverse()	
				print 'clave: %s -UA: %s - VAL: %s' % (clave,  z[0], z[1])
				r.zincrby(clave, z[0], z[1] )
			input_file.close()
	

@hosts('root@204.228.236.6')
def write_data():
	#IPS
	os.remove("webaccesstat.txt")
	r = redis.Redis("localhost", port=6379)
	c= "*******************************************\n"
	c+="**      IPS CON MAS CONEXIONES          **\n"
	c+= "*******************************************\n"
	c+= 'IP'+'\t\t'+'Conex.'+'\t'+'DNS'+'\t\t\t'+'\n'
	ips=r.zrange("ip", 0, -1,withscores=True)
	ips.reverse()
	for i in range(0, 15):
		print ips[i][0], ips[i][1]
		c+=ips[i][0]+'\t'+str(ips[i][1])+'\t'+nslooky(ips[i][0])+'\t\t\t'+'\n'
	
	write_file(c)
	write_file('\n\n')

	d=  "*******************************************\n"
	d+= "** USER AGENTS NO CONVENCIONALES 	 **\n"
	d+= "*******************************************\n"
	d+= 'User Agent'+'\t\t'+'Cantidad'+'\n'
	uas=r.zrange("ua", 0, -1,withscores=True)
	uas.reverse()
	for i in uas:
		if len(i[0]) <25 :
			print i[0].strip(), i[1]
			#length(user_agent)<20 or  user_agent like '%.com%'
			d+=i[0].strip()+'\t\t'+str(i[1])+'\n'
	
	write_file(d)
	write_file('\n\n')
	send_mail()

@parallel(pool_size=10)
def delete_data():
	run("rm -f /usr/local/nginx/logs/*.txt")
	



	
	
	
	
	
	
	
	
	
