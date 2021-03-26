import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
#logging.debug('This is a log message.')

try:  
    import cPickle as pickle  
except ImportError:  
    import pickle  
   
fichero = file("datos.dat", "w")  
animales = ["pitonico", "mono", "camello"]  
 
 
pickle.dump(animales, fichero, 2)  
fichero.close() 
 


fichero = file("datos.dat")  
animales2 = pickle.load(fichero)  
logging.debug('Animale2 vale %s\n',animales2)
fichero.close() 

