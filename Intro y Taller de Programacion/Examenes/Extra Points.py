"""
*********************************************************************
		Instituto Tecnológico de Costa Rica

		    Ingeniería en Computadores

 Lenguaje: Python 3.4.2
 Autor: Pablo Garcia Brenes 
 Versión: 1.0
 Fecha Última Modificación: Mayo 6/2015
 Entradas:Angulo en grados, sen o cos en grados, y N
 Salida: Tangente
 Restricciones: Solo pueden ser integer
*********************************************************************** """

from math import pi
from math import sqrt
#============= Conversion de Radianes a Grados =================#
def radianes(Grados):#funcion que pasa a radianes
    if isinstance(Grados,int) or isinstance(Grados,float): 
        return rad_res(Grados)
    else:
        return "Digite un numero Real"
def rad_res(Grados): #retorna resultado
    return pi*Grados/180


#============= Factorial ======================#
def factorial(N,result): #Funcion factorial 
    if N<1:
        return result
    else:
        return factorial(N-1,result*N)


#================ Sen =======================#
def Sen(X,N):
    if isinstance(X,int) and isinstance(N,int):
        if N==0:
            return 1
        else:
            return aux_sen(X,N,1,1)
    else:
        return "Error"

def aux_sen(X,N,I,resp):
    if N<I:
        return resp
    else:
        formula= (((-1)**N)/(factorial((2*N)+1,1)))*((radianes(X))**((2*N)+1))
        return aux_sen(X,N-1,I,resp+formula)

#================ Cos ===========================#
def Cos(X,N):
    if N in range (10,20) or N==20:
        if N==0:
            return 1
        else:
            return aux_cos(X,N,1,1)
    else:
        return "Numero debe estar entre 10 y 20"

def aux_cos(X,N,I,respuesta): #recursiva de sen
    if N<I:
        return respuesta
    else:
        formula=(((-1)**N))/(factorial((2*N),1))* (radianes(X)**(2*N))
        return aux_cos(X,N-1,I,respuesta+formula)

#================== Tan===========================#

def Tan(Ang,N,SenAng,CosAng):
    if (isinstance(Ang,int)or isinstance(Ang,float)) and isinstance(N,int):
        if CosAng==""or CosAng=="0": # Verifica si es cos el que esta vacio
            Coseno= sqrt(1-Sen(Ang,N)**2)#Saca el cos a partir de despeje de la formula
            Tangente= SenAng/Coseno
            return "La Tangente es de: "+str(Tangente)
        elif SenAng=="0"or SenAng=="":# Verifica si es sen el que esta vacio
            Seno=sqrt(1-(Cos(Ang,N)**2)) #Saca el cos a partir de despeje de la formula
            Tangente= Seno/CosAng
            return "La Tangente es de: "+str(Tangente)
        
    
