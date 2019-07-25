"""
* * * * * * * * * * * * * * * * * * * * * 
* Complemento a la base disminuida.     *
* Input:                                *
*   - num: numero para aplicarle el     *
*          complemento.                 *
* Output:                               *
*   El complemento a la base disminuida.*
* * * * * * * * * * * * * * * * * * * * *
 """
 #Author: Pablo Garcia
def comple_verf(num):
    if isinstance(num,float) or isinstance(num,int):
        string=str(num)
        x= list(string)
        return aux_comple_dis(x,0,0,False,num)
    else:
        return "Por Favor Ingrese un numero."
    
def aux_comple_dis(x,enteros,fracs,flag,numero):
    if x==[]:
        return comple_dis(enteros,fracs,numero)
    else:
        try:
            if flag== False:
              int(x[0])
              return aux_comple_dis(x[1:],enteros+1,fracs,False,numero)
            else:
              int(x[0])
              return aux_comple_dis(x[1:],enteros,fracs+1,flag,numero)
        except:
            return aux_comple_dis(x[1:],enteros,fracs,True,numero)

def comple_dis(enteros,fracs,num):
    integ=enteros
    frac=fracs
    formula= 10**integ-num-10**(-frac)
    return formula
                

######comple_verf(88.88)


"""
* * * * * * * * * * * * * * * * * * *
* Complemento a la base.            *
* Input:                            *
*   - num: numero para aplicarle el *
*          complemento.             *
* Output:                           *
*   El complemento a la base.       *
* * * * * * * * * * * * * * * * * * *
"""
def comple_norm_verf(num):
    if isinstance(num,float) or isinstance(num,int):
        string=str(num)
        x= list(string)#Convierte el numero a una lista para poder separa enteros y fraccionales
        return aux_comple_dis(x,0,0,False,num)  #Retorna el Flase para que indique que esta contando enteros
    else:
        return "Por Favor Ingrese un numero."
    
def aux_comple_dis(x,enteros,fracs,flag,numero):
    if x==[]:
        return comple_dis(enteros,fracs,numero)
    else:
        try:
            if flag== False:  #Si esta contando enteros
              int(x[0])
              return aux_comple_dis(x[1:],enteros+1,fracs,False,numero)
            else:  #Cuenta los fraccionales
              int(x[0])
              return aux_comple_dis(x[1:],enteros,fracs+1,flag,numero)
        except:
            return aux_comple_dis(x[1:],enteros,fracs,True,numero) # Aqui llega cuando entra el punto y cambia a True para que comienze a contar fraccionales


def comple_dis(enteros,fracs,num): #Aplica formula
    integ=enteros
    frac=fracs
    formula= 10**integ-num
    return formula
                
