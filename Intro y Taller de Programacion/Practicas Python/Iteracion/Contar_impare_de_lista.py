#Author: Pablo Garcia
def conta_imp(lista):
    if isinstance(lista,list):
        return aux_cont(lista,0)
    else:
        return "Error"

def aux_cont(lista,cont):
    while lista!=[]:
        if lista[0]%2==1:
            cont+=1
            lista=lista[1:]
        else:
            lista=lista[1:]
    return cont
                 
                 
