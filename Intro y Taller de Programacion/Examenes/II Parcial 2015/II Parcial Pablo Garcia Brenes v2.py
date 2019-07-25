"""
*********************************************************************
		Instituto Tecnológico de Costa Rica

		    Ingeniería en Computadores


Lenguaje: Python 3.4.2
Autor: Pablo David Garcia Brenes
Versión: 2.0
Fecha Última Modificación: Mayo 2/2015
Carne:2015083681

Profesor: Milton Villegas Lemus
Curso: Introduccion a la Programacion

II Parcial
 
*********************************************************************** """
#Funcion:Determina que numero esta escrito en la hilera
#Entrada: Hilera con numeros escritos con inicial en minuscula o mayuscula y lo demas en minuscula
#Salida: Los numeros que estaban escritos en la entrada con palabras.

def letter2num(Hilera):
    if isinstance(Hilera,str):
        if Hilera=="": # Se agrego esta condicion por si ingresa Hilera vacia
            return "Hilera no debe estar vacia."
        else:
            return aux_letter(Hilera,[])
    else:
        return "Error:el parametro no es del tipo esperado hilera de caracteres."

def aux_letter(Hilera,lista):
    if Hilera=="":
        return num_final(lista,len(lista)-1,0)  
    else:
        if Hilera[0]=="U" or Hilera[0]=="u":
            lista.append(1)
            return aux_letter(Hilera[3:],lista) #Se saco el append del parametro en todas las siguientes lineas
        elif Hilera[0]=="D" or Hilera[0]=="d":
            lista.append(2)
            return aux_letter(Hilera[3:],lista)
        elif Hilera[0]=="T" or Hilera[0]=="t":
            lista.append(3)
            return aux_letter(Hilera[4:],lista)
        elif Hilera[0]=="O" or Hilera[0]=="o":
            lista.append(8)
            return aux_letter(Hilera[4:],lista)
        elif Hilera[0]=="N" or Hilera[0]=="n":
            lista.append(9)
            return aux_letter(Hilera[5:],lista)
        elif Hilera[0]=="S" or Hilera[0]=="s":
            if Hilera[1]=="e":
                lista.append(6)
                return aux_letter(Hilera[4:],lista)
            else:
                lista.append(7)
                return aux_letter(Hilera[5:],lista)
        elif Hilera[0]=="C" or Hilera[0]=="c":
            if Hilera[1]=="e":
                lista.append(0)
                return aux_letter(Hilera[4:],lista)
            elif Hilera[1]=="u":
                lista.append(4)
                return aux_letter(Hilera[6:],lista)
            else:
                lista.append(5)
                return aux_letter(Hilera[5:],lista)

def num_final(lista,indice,numero):
    if lista==[]:
        return numero
    else:
        massig=lista[0]
        num=massig*(10**indice)
        return num_final(lista[1:],indice-1,numero+num)

    
#letter2num("tresTrescincoCuatroSieteDos")

#=============================================================================#
#Calcula la mitad de Pi
#Entrada un numero entero entre 1 y 100
#Salida calculo con ese numero ingresado
def pi_medio(N):
    if isinstance(N,int):
        if N in range(1,100) or N==100:
            return aux_pi(N,1) #cambie 0 por 1
        else:
            return "Error."
    else:
        return "Error1."

def aux_pi(N,resp):
    if N==0:
        return resp
    else:
        formula=((2**N)*(facto(N,1))**2)/facto((2*N+1),1) #en facto me falto un parametro
        return aux_pi(N-1, resp+formula)

def facto(N,result):
    if N==1:
        return result
    else:
        return facto(N-1, result*N)

#pi_medio(1)
#==================================================================================#
#Funcion que calcula el Area y Volumen de una Esfera
#Entradas: Radio y el valor de N
#Salidas: El Volumen y Area en una lista 
def volu_area(Radio,N):
    if isinstance(Radio,int)or isinstance(Radio,float):
        if Radio>0:
            if isinstance(N,int):
                if N in range(0,100) or N==100:
                    return aux_vol(Radio,N,[])
                else:
                    return"El valor de N para calcular Pi debe ser mayor que 0."
            else:
                return "N debe ser entero."
        else:
            return "Radio debe ser mayor que 0."
    else:
        return "Radio debe ser numerico."

def aux_vol(Radio,N,respuesta):
    if Radio<=0:
        return respuesta
    else:
        Area= 4*(pi_medio(N)*2)*(Radio**2)     #En pi_medio lo multiplique por 2
        Volumen=(4*(pi_medio(N)*2)*(Radio**3))/3
        lista=[Volumen,Area]
        respuesta=lista
        return aux_vol(Radio-Radio,N,respuesta)

#volu_area(8,100)
    
#=================================================================================#
#Funcion que divide utilizando restas solamente
#Entradas: Numeros entros: Dividendo y Divisor
#Salidas:El Dividendo, Divisor, Cociente,Residuo, y el Residuo en Binario
        
def mi_divi(Dividendo,Divisor):
    if isinstance(Dividendo,int) and isinstance(Divisor,int):
        if Divisor!=0:
            return aux_divi(Dividendo,Divisor)
        else:
            return "No se permite la division entre 0."
    else:
        return "Las entradas debe ser enteros."

def aux_divi(Dividendo,Divisor):
    if Dividendo>0 and Divisor>0:
        return aux_pos(Dividendo,Divisor,Dividendo,0,Divisor)
    elif Dividendo<0 and Divisor>0:
        abso=-Dividendo
        return aux_pos(abso,Divisor,Dividendo,0,Divisor)
    elif Dividendo>0 and Divisor<0:
        abso=-Divisor
        return aux_pos(Dividendo,abos,Dividendo,0,Divisor)
    else:
        abso=-Divisor
        absoD=-Dividendo
        return aux_pos(absoD,abso,Dividendo,0,Divisor)

def aux_pos(Dividendo,Divisor,original,Cociente,originalD):
    if Dividendo<Divisor:
        return final(original,originalD,Cociente,Dividendo,0) #agregue parametro 0
    else:
        Dividendo=Dividendo-Divisor
        return aux_pos(Dividendo,Divisor,original,Cociente+1,originalD)

def final(Dividendo,Divisor,Cociente,Residuo,Binario):
    if Dividendo<0:   #Agregue este if para que retorne Cociente negativo por falta de tiempo no lo hice
        Cociente=-Cociente
        Binario= bina(Residuo,0,0)
        tupla= (Dividendo,Divisor,Cociente,Residuo,Binario) #quite la palabra tuple
        return tupla
    else:
        Binario= bina(Residuo,0,0)
        tupla= (Dividendo,Divisor,Cociente,Residuo,Binario) #quite la palabra tuple
        return tupla

def bina(Residuo,resp,indice):
    if Residuo<=0: #Agregue igual
        return resp
    else:
        res=(10**indice)*(Residuo%2)
        return bina(Residuo//2,resp+res,indice+1)
