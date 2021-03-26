#! /usr/bin/env python

def fibiter(n): # Escribe n nmeros de Fibonacci
    "Escribe n nmeros de Fibonacci."    
    a,b = 0,1           #Asignacin mltiple      
    salida=[]
    for x in range(n):  #Creamos una secuencia 1,2,...,n con range
        print b,        # Escribimos en una sola lnea
        salida.append(b)
        a, b = b, a+b
        
    return salida

def fibrec(n):
    "Escribe n nmeros de Fibonacci."
    if (n < 2):
        return n
    else:
        return fibrec(n-1) + fibrec(n-2)


# El fibrec(n)desbordamiento se produce con valores mayores de 45

fibiter(2000)
