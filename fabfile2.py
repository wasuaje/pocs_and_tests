from fabric.api import *

env.roledefs = {
    'web': ['root@204.228.236.6', 'root@204.228.236.13', 'root@204.228.236.17'],
    'app': ['root@204.228.236.2', 'root@204.228.236.7']
}

def host_type():
    run('uname -s')

@parallel
def num_conx():
    run('netstat -ntu|wc -l')
