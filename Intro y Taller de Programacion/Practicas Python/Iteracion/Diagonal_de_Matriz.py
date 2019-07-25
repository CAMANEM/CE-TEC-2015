#Author: Pablo Garcia

def diagonal(matriz):
    if isinstance(matriz,list) and isinstance(matriz[0],list):
        return aux_diag(matriz,0,[])
    else:
        return "Erorr"

def aux_diag(matriz,i,diag):
    j=0
    suma=0
    while i<len(matriz):
        temp=matriz[i][i]
        diag=diag+[temp]
        i+=1
        while j<i:
            suma=diag[j]+suma
            j+=1
    return suma
