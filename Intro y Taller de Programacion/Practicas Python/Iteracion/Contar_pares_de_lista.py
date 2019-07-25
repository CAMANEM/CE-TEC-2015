#Author: Pablo Garcia

#Contar Pares de una lista con while
def cont_par(Lista):
    if isinstance(Lista,list):
        cont=0
        while Lista!=[]:
            if Lista[0]%2==0:
                cont+=1
                Lista=Lista[1:]
            Lista=Lista[1:]
        return cont
    
#Contar Impares de una lista con for
def Contar_pares(Lista):
    if isinstance(Lista,list):
        cont=0
        for i in range(0,len(Lista)):
            if Lista[i]%2==0:
                cont+=1
        return cont
                       
