def for_general(num):
    if isinstance (num,int)or isinstance (num,float):
        string=str(num)
        x= list(string)
        return lenn_numero(x,0,0,False,num)
    else:
        return "Entrada no valida, por favor ingrese un numero entero"

def lenn_numero(x,enteros,fracs,flag,numero):
    if x==[]:
        return formula_gen(enteros,fracs,numero,False) #Condicion de Finalizacion 1
    else:
        try:
            if flag== False:
                int(x[0])
                return lenn_numero(x[1:],enteros+1,fracs,False,numero) #Va contando los enteros
            else:
                int(x[0])
                return lenn_numero(x[1:],enteros,fracs+1,flag,numero) #Cuenta los fraccionales
        except:
            return lenn_numero(x[1:],enteros,fracs,True,numero) # Detecta cuando terminan enteros y empieza los fraccionales
        

def formula_gen(enteros,fracs,numero,flag):
    string_num=str(numero)
    num=list(string_num)

    try:
        if flag== False:
            int(num[0])
            formula=num[0]**(enteros-1)*8
            return formula+ formula_gen
        else:
            formula= num[0]**(enteros-1)*8
            return
        
        
