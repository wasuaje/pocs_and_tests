import procpy
pp = procpy.Proc()
for pid in pp.pids:
    if pp.procs[pid]['cmd'] == 'apache2':
        print pp.procs[pid]['tid'] 