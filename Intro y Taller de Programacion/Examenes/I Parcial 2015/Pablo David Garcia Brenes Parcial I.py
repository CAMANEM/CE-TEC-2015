"""
*********************************************************************
		Instituto Tecnológico de Costa Rica

		    Ingeniería en Computadores


Lenguaje: Python 3.4.2
Autor: Pablo David Garcia Brenes
Versión: 1.0
Fecha Última Modificación: Abril 20/2015
Carne:2015083681

Profesor: Milton Villegas Lemus
Curso: Introduccion a la Programacion

I Parcial
 
*********************************************************************** """
#Funcion: Saca paridad, Cuenta si cantidad de 1 es divisible por 3, Cuenta si cantidad de 0 es divisible por 5
#Entrada: Hilera
#Salida: Paridad, 1 es divisble por 3, 0's son divisbles por 5

def paridad_par_1d3_0d5(Hilera): #Saca la paridad 
    if Hilera==[]:
        return "La Lista no debe ser nula."
    else:
        #Div_aux(Hilera ya con la paridad, Cantidad de 1 en la hilera, Cantidad de 0 en la hilera)
        return div_aux(paridad_par_aux((Hilera),aux_paridad(Hilera)),(div0(paridad_par_aux(Hilera,aux_paridad(Hilera)))),(div1(paridad_par_aux(Hilera,aux_paridad(Hilera)))))
      #esta funcon llama a todas las demas 

def aux_paridad(Hilera):
    if Hilera==[]:  #Agregue :
        return 0
    else:
        if Hilera[0]==1:
            return 1+aux_paridad(Hilera[1:])
        else:
            return aux_paridad(Hilera[1:])

def paridad_par_aux(Hilera,cant):    #Cant es la cantidad de 1 que contiene la hilera
    if cant%10==1:
        return Hilera +[1]
    else:
        return Hilera+[0]

def div0(Hilera):
    if Hilera==[]: #Agregue ==
        return 0 #Cambie Hilera por 0
    else:
        if Hilera[0]==0:
            return 1+div0(Hilera[1:])
        else:
            return div0(Hilera[1:])
        
def div_aux(Hilera,Ceros,Unos):
    Si1= "unos SI div por 3"
    No1= "unos NO div por 3"   #Error sintaxis, No puse oraciones entre comillas
    Si0= "ceros SI div por 5"
    No0= "ceros NO div por 5"
    if Ceros%5==0:
        if Unos%3==0:
            return [Hilera]+[Si1]+[Si0]
        else:
            return [Hilera]+[No1]+[Si0]
    else:
        if Unos%3==0: #Agregue :
            return [Hilera]+[Si1]+[No0]
        else:
            return [Hilera]+[No1]+[No0] # Hiler paso a Hilera

def div1(Hilera):
    if Hilera==[]: #Agregue ==
        return 0 #Cambie Hilera por 0
    else:
        if Hilera[0]==0:
            return div1(Hilera[1:])
        elif Hilera[0]==1: #Cambio else Hilera[0]==1: por elif Hilera[0]==1:
            return 1+div1(Hilera[1:])
#======================================================================================================#
#Formula de Gravitacion Universal
#Entradas: Fuerza, Masa1 y Masa2, Radio (Con una de ellas como incognita)
#Salida:La incognita
def gravitacion_universal(Fi,m1,m2,r):
    if Fi=='' or m1=='' or m2=='' or r=='':
        if Fi=='' and r=='':
            return "Parametros invalidos."
        else:                          # El return estaba en misma linea que el else,NO TIRABA ERROR POR ESo, pero lo baje 
            return aux_grav(Fi,m1,m2,r)
    else:
        return "Incorrecto debe existir una incognita"

def aux_grav(Fi,m1,m2,r): #Agregue Lineas que convierten de string a float
    G=(6.6738*10)**(-11) #constante de G
    if Fi=='':  #Si debemos calcular la Fueza
        m1=float(m1)
        m2=float(m2)
        r=float(r)
        Fuerza=(G*m1*m2)/(r**2) #Calcula la Fueza
        string= "La fuerza de atraccion es de:"
        return string + str(Fuerza)
    elif m1=='':
        Fi=float(Fi)
        m2=float(m2)
        r=float(r)
        masa=(Fi*(r**2))/(G*m2) 
        string= "La masa es de:"
        return string+ str(masa)
    else:
        m1=float(m1)
        m2=float(m2)
        Fi=float(Fi)
        string="El radio entre masas es de:" #agregue esta linea
        radio=((G*m1*m2)/(Fi))**(1/2)
        return string + str(radio) #puse el return
#============================================================================================#

def num_e_aux(N):
    if isinstance(N,int):
        if N in range (1,24) or N==24:
            return aux_e(N,1)
        else:
            return "Numero N debe estar entre 0 y 24." # La palabra "entre" estaba mal escrita
    else:
        return "N debe ser un numero entero."

def aux_e(N,I): #Error de sintaxis, Cambie 1 por I
    if N<1:
        return 1
    else:
        formula= (1)/(factorial(N))
        return formula+ aux_e(N-1,1)

def factorial(N):
    if N==0:
        return 1
    else:
        return N * factorial(N-1)

#========================== Parte B =====================================================

def num_e_C9_aux(N,cantiDigitos):
    if N==1 and cantiDigitos==0:
        return 8
    elif N==0 and cantiDigitos==0:
        return 9
    else:
        N=N*(10**(cantiDigitos)) #Agregue estas 2 lineas
        N=int(N)
        return aux_C9(N,cantiDigitos)

def aux_C9(N,cantiDigitos):
    if N==0:
        return 0
    else:
        menossig= N%10
        comple=9-menossig
        num= comple*(10**(-cantiDigitos))
        return num+ aux_C9(N//10,cantiDigitos-1)

def CantiDigitos(N):
    Lista= list(str(N)) #Agregue esta linea
    Cant= len(Lista)
    Cant= Cant-2
    return Cant

#======================== Parte C ===========================================================

def number_minus_eu(Number):
    if isinstance(Number,int) or isinstance(Number,float):
        return aux_number(Number)
    else:
        return "Se debe ingresar un numero entero o fraccional" #Agregue la palabra ingresar

def aux_number(Number):
    Comple_e= num_e_C9_aux(num_e_aux(20), CantiDigitos(num_e_aux(20)))
    if Number>0:
        Operacion= Number+ Comple_e  #Elimine algunas lineas
        return Operacion
    else:
        Number1=int(Number) #Agregue linea
        Lista= list(str(Number1)) #agregue linea
        lenn= len(Lista) -1
        formula=(10**lenn)+Number
        Operacion= formula+ (num_e_C9_aux(num_e_aux(20),CantiDigitos(num_e_aux(20))))
        return Operacion
