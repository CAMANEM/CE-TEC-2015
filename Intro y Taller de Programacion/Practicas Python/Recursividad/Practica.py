def punt(Lista):
    if isinstance(Lista,list):
        return promedios(Suma1(Lista),Suma2(Lista,mayor1(Lista,Lista[0]),menor1(Lista,Lista[0])))
    else:
        return "Error"
def mayor1(Lista,mayor):
    if Lista ==[]:
        return[]
    else:
        Lista[0]=int(Lista[0])
        if Lista[0]>mayor:
            return mayor(Lista[1:],Lista[0])
        else:
            return mayor1(Lista[1:],mayor)

def menor1(Lista,menor):
    if Lista ==[]:
        return 0 
    else:
        if Lista[0]<menor:
            return mayor([Lista[1:]],[Lista[0]])
        else:
            return mayor([Lista[1:]],mayor)
       


def Suma1(Lista):
    if Lista==[]:
        return 1
    else:
        Num=int(Lista[0])
        return Num+ Suma1(Lista[1:])
def Suma2(Lista,mayor,menor):
    if Lista==[]:
        return 1
    else:
        if Lista[0]==mayor:
            return Suma2(Lista[1:], "",menor)
        elif Lista[0]==menor:
            return Suma(Lista[1:],mayor,"")
        else:
            Num= int(Lista[0])
            return Num+ Suma2(Lista[1:],mayor,menor)  

def promedios(prom1,prom2):
    prom1= prom1/7
    prom2= prom2/5
    diferencia=prom1-prom2
    return prom1,prom2,diferencia
