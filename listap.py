import commands, os, string,sys,subprocess

def run_cmd(comando):
	p = subprocess.Popen(comando, shell=True, stdout=subprocess.PIPE)
	out = p.stdout.read().strip()
	return out  #This is the stdout from the shell command

#program ="firefox"
program =sys.argv[1]
#perform a ps command and assign results to a list
output = commands.getoutput("ps -fea|grep " + program + "|grep -v 'grep'" + "|grep -v 'python'")
proginfo = string.split(output)

a=[]
#print proginfo
#print len(proginfo)
for i in xrange(len(proginfo)) :
	if proginfo[i]=="wasuaje":
		a.append(proginfo[i+1])

for ID in a:
	comando="kill -9 "+ID
	#print comando
	run_cmd(comando)


