"""
*******************************************************************
        Instituto Tecnológico de Costa Rica

            Ingeniería en Computadores


 Lenguaje: Python 3.4.2
 Autor: Pablo Garcia Brenes 
 Versión: 1.1
 Fecha Última Modificación: Mayo 3/2015

Descripcion: 
    -vec_vec: Multiplica un vector por otro vector. 
    -sum_vec: Suma dos vectores. 
Entrada:
    - Vec1: Primer vector.
    - Vec2: Segundo vector.
Salida: 
    - vec_vec: Un escalar resultado de la multiplicacion.
    - sum_vec: Un vector resultado de la suma.

Restricciones:
    - Debe contener enteros en cada vector.
 
******************************************************************* """


#Multiplicacion de Vector por Vector
#Retorna un escalar
def vec_vec(Vec1,Vec2):
    if isinstance(Vec1,list) and isinstance(Vec2,list):
        if len(Vec1)== len(Vec2):
            return aux_vec(Vec1,Vec2,0)
        else:
            return "La longitud de los vectores no es igual."
    else:
        return "No es valido el vector."

def aux_vec(Vec1,Vec2, result):
    if Vec1==[]:
        return result
    else:
        if isinstance(Vec1[0],int) and isinstance(Vec2[0],int):
            result=result+(Vec1[0]*Vec2[0])
            return aux_vec(Vec1[1:],Vec2[1:],result)
        else:
            return "No son valores numericos."

#Suma de 2 vectores
#Se suma cada indice con cada indice

def sum_vec(Vec1,Vec2):
    if isinstance(Vec1,list) and isinstance(Vec2,list):
        if len(Vec1)== len(Vec2):
            return aux_sum(Vec1,Vec2,[])
        else:
            return "La longitud de los vectores no es igual."
    else:
        return "No es valido el vector."

def aux_sum(Vec1,Vec2,Vecfinal):
    if Vec1==[]:
        return Vecfinal
    else:
        if isinstance(Vec1[0],int) and isinstance(Vec2[0],int):
            suma=Vec1[0]+Vec2[0]
            Vecfinal.append(suma)
            return aux_sum(Vec1[1:],Vec2[1:],Vecfinal)
        else:
            return "No son valores numericos."
            


            
            
