## ir agregando import y funciones con las prueba a realizar
import commands

def comandos_columnas():
    mount = commands.getoutput('ls -lah /home/wasuaje | grep -v total')
    lines = mount.split('\n')
    for line in lines:
        columns=line.split()
        a = len(columns)
        for i in range(0,a):
            print columns[i]+'\t',
        print '\n'
    #points = map(lambda line: line.split()[2], lines)
    #print points


comandos_columnas()

 