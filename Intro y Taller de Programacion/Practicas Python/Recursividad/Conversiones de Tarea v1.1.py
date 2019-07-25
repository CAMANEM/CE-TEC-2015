def conv2 (x):
    if isinstance (x,int):
        return conv2_1(x)
    else:
       return "Entrada no valida, por favor ingrese un numero entero"
    
def conv2_1(x):
    conver= "{0:b}".format(x)  #otra forma de usar bin() para que retorne solamente numeros
    return conver

def sumabase2(x,y): #suma ambas cifras
    suma= x+y
    return conv2(suma)

#########   BASE 8 ###########
def conv8 (x):
    if isinstance (x,int):
        return conv8_1(x)
    elif isinstance (x,float):
        pasarint= int(x)
        return conv8_1(pasarint)
    
    else:
       return "Entrada no valida, por favor ingrese un numero entero"

def conv8_1(x):
    conver= "{0:o}".format(x)
    return conver

def sumabase8 (x,y):
    suma= x+y
    return sumabase8


######### DECIMAL-BASE 16 ############
def sumahex(Numero1,Numero2):
    if isinstance(Numero1,str) and isinstance(Numero2,str):
        return conv16(conv_a10(Numero1) + conv_b10(Numero2)) #Suma aqui en decimal 
    else:
        return "Ingrese el numero hexadecimal dentro de un string."

def conv16(x): #Convierte de Base 10 a hexadecimal
    try:
        pasar_ent= int(x)
        conver= "{0:X}".format(pasar_ent) #Funcion de hex pero de otra forma
        return conver
    except:
        return "Ingrese numeros enteros."

########### BASE 16 -DECIMAL ###########

def conv_a10(X): #Convierte de hexadecimal a decimal
    try:
        enstr= str(X) #Inserta los valores dentro de un string 
        pasar10= int(enstr,16) 
        return pasar10
    except:
        return "Ingrese un numero hexadecimal"