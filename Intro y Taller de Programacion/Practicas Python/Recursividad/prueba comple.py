def Comple():
        digito= int(cifra2.get())
        
        def Operacion(numero):
            if isinstance (numero,int):
                return devolverB2(comple_norm_verf(conv2(numero)),1)
            else:
                return "Verifique las entradas"
        
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
                    return aux_comple_dis(x[1:],enteros,fracs,True,numero) # Aqui llega cuando entra el punto y cambia a True para que comienze a contar fraccionale    
        def comple_dis(enteros,fracs,num):
            integ=enteros
            frac=fracs
            formula= 10**integ-num#-10**(-frac) #Aplica formula
            return formula
        
        def seg_conv8 (digito2):
            if isinstance (digito2,int): #verifica que sea int
               return aux_seg_conv8(digito2,0)
            elif isinstance (digito2,float): #convierte a int
                pasarint= int(digito2)
                return aux_seg_conv8(pasarint)
            else:
               return "Entrada no valida, por favor ingrese un numero entero"
    
        def aux_seg_conv8(digito2,expon):
            if digito2==0:
                return 0 # condicion de terminacion 1, si no hay mas que dividir retorna todo con el ultimo residuo
            else:
                return (digito2%10*8**expon) + aux_seg_conv8(digito2//10,expon+1)

        def devolverB8(decimal,expon):
            try:
                if decimal==0:
                    return 0
                else:
                    return (decimal%8*expon) + devolverB8(decimal//8,expon*10)
            except:
                return "Entrada no valida, por favor verifique sus entradas."                
    button_CD= Button(vent_comenzar,command=CompDis, text="Calcular")
    button_CD.grid(row=20,column=7)

    
########## conv de base 8
def seg_conv8 (digito2):
            if isinstance (digito2,int): #verifica que sea int
               return aux_seg_conv8(digito2,0)
            elif isinstance (digito2,float): #convierte a int
                pasarint= int(digito2)
                return aux_seg_conv8(pasarint)
            else:
               return "Entrada no valida, por favor ingrese un numero entero"
    
        def aux_seg_conv8(digito2,expon):
            if digito2==0:
                return 0 # condicion de terminacion 1, si no hay mas que dividir retorna todo con el ultimo residuo
            else:
                return (digito2%10*8**expon) + aux_seg_conv8(digito2//10,expon+1)

        def devolverB8(decimal,expon):
            try:
                if decimal==0:
                    return 0
                else:
                    return (decimal%8*expon) + devolverB8(decimal//8,expon*10)
            except:
                return "Entrada no valida, por favor verifique sus entradas."

