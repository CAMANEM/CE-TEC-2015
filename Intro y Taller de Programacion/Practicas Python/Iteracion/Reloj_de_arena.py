"""**********************
Iterate over the matrixs first and last row
as well as both diagonals.

Author: Pablo Garcia
*************************"""
def reloj_arena(matriz):
    if len(matriz)==len(matriz[0]):
        return aux_reloj(matriz,len(matriz)-1,0,[],[],[],[])
    else:
        return "error"

def aux_reloj(matriz,n,i,impares,diag1,diag2,temp):
    while n>=0:
        if matriz[len(matriz)-1][n]%2==1:
            impares=impares+[matriz[len(matriz)-1][n]]
        n-=1
        while i<=len(matriz[0])-1:
            if matriz[0][i]%2==1:
                temp=temp+[matriz[0][i]]
            i+=1
    temp.reverse()
    n=len(matriz)-2
    i=1
    while n>=0:
        if matriz[n][i]%2==1:
            diag1=diag1+[matriz[n][i]]
            if matriz[i][i]%2==1:
                diag2=diag2+[matriz[i][i]]
        n-=1
        i+=1
    final=impares+diag1+temp+diag2
    return final
        
    
            

