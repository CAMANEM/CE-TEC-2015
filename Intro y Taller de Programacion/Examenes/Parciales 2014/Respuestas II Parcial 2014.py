def base4to2(ListaBase4):
    if isinstance(ListaBase4,list):
        if ListaBase4==[]:  
            return []
        else:
            return aux_base4to2(ListaBase4,[]) 
    else:
        return "Debe ser una lista."

def aux_base4to2(Lista,Nueva):
    if Lista==[]:
        return Nueva
    else:
        
        if Lista[0]== '0' or Lista[0]=='3' or Lista[0]=='2' or Lista[0]=='1':
            if Lista[0]=='0':
                Nueva= Nueva+["0"]
                Nueva= Nueva+["0"]
                return aux_base4to2(Lista[1:],Nueva)
            elif Lista[0]=='1':
                Nueva= Nueva+["0"]
                Nueva= Nueva+["1"]
                return aux_base4to2(Lista[1:],Nueva)
            elif Lista[0]=='2':
                Nueva= Nueva+["1"]
                Nueva= Nueva+["0"]
                return aux_base4to2(Lista[1:],Nueva)
            else:
                Nueva= Nueva+["1"]
                Nueva= Nueva+["1"]
                return aux_base4to2(Lista[1:],Nueva)
        else:
            Nueva=Nueva+["Error Base 4."]
            return aux_base4to2(Lista[1:],Nueva)

def string2num(ListaBin):
    if isinstance(ListaBin,list):
        return aux_string(ListaBin[::-1],0,0)
    else:
        return "El Argumento debe ser una lista."

def aux_string(ListaBin,Bin,exp):
    if ListaBin==[]:
        return Bin
    else:
        if ListaBin[0]=='0':
            return aux_string(ListaBin[1:],Bin,exp+1)
        else:
            Bin= Bin+ 1*10**exp
            return aux_string(ListaBin[1:],Bin,exp+1)
def pi_medio(N):
    return aux_pi(N,1)
def aux_pi(N,I):
    if N<I:
        return 1
    else:
        formula=(((2**N)*((factorial(N))**2)))/(factorial((2*N)+1))
        return formula+aux_pi(N-1,I)
    
def factorial(N): #Agregue parametros
    if N==0: #Agregue un =
        return 1 #agregue retornar a la formula
    else:
        return N*factorial(N-1)
def volu_area(Radio,Altura):
    if isinstance(Radio,int):
        if Radio>0:
            return aux_vol_area(Radio,Altura,[]) #Agregue []
        else:
            return "Radio debe ser mayor que 0."
    else:
        return "Radio debe ser numerico."

def aux_vol_area(Radio,Altura,Listas):
    g= (((Altura**2)+(Radio**2)) **(1/2))
    Area=(((pi_medio(100)*2)*(Radio**2))+(pi_medio(100)*2)*(Radio)*(g))
    Vol= (((pi_medio(100)*2)*(Radio*2)*(Altura))/3)
    Listas= Listas+[Vol]
    Listas= Listas+[Area]
    return Listas
           
