"""
*******************************************************************
        Instituto Tecnológico de Costa Rica

            Ingeniería en Computadores


 Lenguaje: Python 3.4.2
 Autor: Pablo Garcia Brenes 
 Versión: 1.1
 Fecha Última Modificación: Enero 2019

Descripcion: 
    -restabase2: Resta dos numeros que esten en base 2.
Entrada:
    - X: Primer numero en binario.
    - Y: Segundo numero en binario.
Salida: 
    - restabase2: Un enter resultado de la resta.

Restricciones:
    - Deben ser numeros binarios enteros.
 
******************************************************************* """


#Funcion Principal resta ambas cifras
def restabase2(X,Y):                                                    
    if isinstance(X,int) and verf_bin(X):
        if isinstance(Y,int) and verf_bin(Y):
            return devolverB2(conv2(X) - conv2(Y),1)                #Pasa a base 10 resta ambos y vuelve a base 2
        else:
            return "Entrada no valida, por favor revise las entradas."
    else:
        return "Entrada no valida, por favor revise las entradas."

#Validacion       
def conv2 (X):                  
    if isinstance (X,int):
        return aux_conv2(X,0)
    else:
       return "Entrada no valida, por favor ingrese un numero entero"

#Convierte a decimal
def aux_conv2(X,expon):                             
    if X==0:
        return 0                                #Condicion de terminacion 1, si no hay mas que dividir retorna todo con el ultimo residuo
    else:
        return (X%10*2**expon) + aux_conv2(X//10,expon+1)               #Aplica formula general

#Verifica que sean bin
def verf_bin(X):                                          
    if X==0:
        return True
    elif X%10!=0 and X%10!=1:
        return False
    else:
        return verf_bin(X//10)

#Devuleve a Binario
def devolverB2(decimal,expon):   
    try:
        if decimal==0:
            return 0
        else:
            return (decimal%2*expon) + devolverB2(decimal//2,expon*10)
    except:
        "Entrada no valida, por favor revise las entradas."