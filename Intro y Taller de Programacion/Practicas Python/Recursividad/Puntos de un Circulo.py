import math
from math import *

def circulo(cantpuntos,Radio):
    if isinstance(cantpuntos,int):
        if cantpuntos>=4:
            angulo=360//cantpuntos
            return aux_circulo(cantpuntos,0,angulo,Radio,True)
        else:
            return "Error debe ser mayor a 4"
    else:
        return "Error ingrese un numero entero."

def aux_circulo(cantpuntos,anguloI,angulo2,Radio,Flag):
    if anguloI>=180:
        return aux_circulo(cantpuntos,0,angulo2,Radio,False)
    else:
        if Flag==True:
            Y= round(Radio*sin(anguloI))
            X= round(Radio*cos(anguloI))
            if cantpuntos==0:
                return []
            else:
                punto= list([[X,Y]])
                return punto+ aux_circulo(cantpuntos-1,anguloI+angulo2,angulo2,Radio,Flag)
        else:
            Y= round(Radio*sin(anguloI))
            X= round(Radio*cos(anguloI))
            if cantpuntos==0:
                return []
            else:
                punto= list([[-X,-Y]])
                return punto+ aux_circulo(cantpuntos-1,anguloI+angulo2,angulo2,Radio,Flag)
        
    
