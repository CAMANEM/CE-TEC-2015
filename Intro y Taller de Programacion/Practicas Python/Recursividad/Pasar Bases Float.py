def conv8 (x):
    if isinstance (x,int):
        return conv8_int(x)
    elif isinstance (x,float):
        return con8_float(x)
    else:
       return "Entrada no valida, por favor ingrese un numero entero"

def con8_float(x):
    y=str(x)          # Convierte entrada en string
    return conv8_float(y.split(".",1))
    ListY= list(y)      # Convierte string en lista
    return aux_float(0,0,ListY,False)

def aux_float(enteros,fracs,x,flag):
    if x==[]:
        return enteros,fracs
    else:
        try:
            int(x[0])
            if flag==False:
                return aux_float(enteros+1,fracs,x[1:],False)
            else:
                int(x[0])
                return aux_float(enteros,fracs+1,x[1:],flag)
        except:
            return aux_float(enteros,fracs,x[1:],True)

def conv8_float(ent_frac):
    enteros=ent_frac[0]
    frac=ent_frac[1]
    def parte_ent(enteros):
        int(enteros)
        if enteros>0 and enteros>7:
            if enteros//8==0 : #si el numero es menor que 2 o igual efectua la operacion
                div= x//8
                res=x%8
                print(res,end="") # condicion de terminacion 1, si no hay mas que dividir retorna todo con el ultimo residuo
            elif enteros//8!=0:
                div= enteros//8
                res=x%8
                print( conv8_float(div), end="")
                return res
        elif enteros>=1 and enteros<8:
            return x #Condicion de terminacion 2
        else:
            return "Error"

    def parte_frac(frac):
        x=str(0.)
        x+frac
        float(frac)
        if frac>0.1:
            return frac
        else:
            multi= frac*8
            return parte_frac(multi)
            
def parte_frac(frac):
        frac//10
        if frac>=0.1:
            return frac
        else:
            multi= frac*8
            return parte_frac(multi)            
            
            
                          
    
        
    
    




def conv8_int(x):
    if x>0 and x>7:
        if x//8==0 : #si el numero es menor que 2 o igual efectua la operacion
            div= x//8
            res=x%8
            print(res,end="") # condicion de terminacion 1, si no hay mas que dividir retorna todo con el ultimo residuo
        elif x//8!=0:
            div= x//8
            res=x%8
            print( conv8_int(div), end="")
            return res
    elif x>=1 and x<8:
        return x #Condicion de terminacion 2
    else:
        return "Error"
