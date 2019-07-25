def a4div3_3div7(hilera):
    if isinstance(hilera,str):
        if hilera[0]=='@':
            if hilera[1]!='@':
                return resultado(div(hilera[1:]),div3(hilera[1:]))
            else:
                return "Error delimitador @ en el intermedio"
        else:
            return " Error no comienza con @."
    else:
        return "error no es hilera."

def div(hilera):
    if hilera=='':
        return 0
    else:
        if hilera[0]=='4':
            return 1+div(hilera[1:])
        else:
            return div(hilera[1:])

def div3(hilera):
    if hilera=='':
        return 0
    else:
        if hilera[0]=='3':
            return 1+div3(hilera[1:])
        else:
            return div3(hilera[1:])
def resultado(cuatros,tres):
    Si4="La cantidad de digitos 4 es divisible por 3"
    No4="La cantidad de digitos 4 no es divisible por 3"
    Si3="La cantidad de digitos 3 es divisible por 7"
    No3="La cantidad de digitos 3 no es divisible por 7"
    if cuatros%3==0:
        if tres%7==0:
            print( Si4+ '\n'+Si3)
        else:
            print(Si4+'\n'+No3)
    else:
        if tres%7==0:
            print( No4+'\n'+ Si3)
        else:
            print(No4+'\n'+ No3)

def vel_ace_t(vi,vf,a,t):
    if vf=="":
        if a=="":
            return "Error existe mas de una incognita."
        else:
            try:
                a=float(a)
                t=float(t)
                vi=float(vi)
                if t<0:
                    return "Error: No definido para timepo Negativo."
                else:
                    return aux_vel(vi,vf,a,t)
            except:
                return "Debe existir una incognita en los parametros."
    else:
        return "Debe existir una incognita en los parametros."
    

def aux_vel(vi,vf,a,t):
    vf= vi+(a*t)
    Velin="Velocidad inicial:"
    Ace="Aceleracion"
    Tiem="Tiempo:"
    Velfin="Velocidad final:"
    print( Velin+ str(vi) +'\n'+ Ace+str(a)+'\n'+Tiem+str(t)+'\n'+Velfin+str(vf))



def cos(X,N):
    if isinstance(X,float):
        if isinstance(N,int):
            if N in range(10,20) or N==20:
                return aux_cos(X,N,1)
            else:
                return "Error, entrada invalida."
        else:
            return "Error, entrada invalida."
    else:
        return "Error, entrada invalida."
def aux_cos(X,N,I):
    if N<I:
        return N+1
    else:
        formula=(((-1)**N)/(facto(2*N)))*((facto(X))**(2*N))
        formula= formula*180/3.14159265
        return formula+aux_cos(X,N-1,I)
def facto(X):
    if X<=0:
        return 1
    else:
        return X*facto(X-1)
    
    
        
        
        
