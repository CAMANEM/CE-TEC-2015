def mult_matrices(Matriz1,Matriz2):
    Matriz2= transpuesta(Matriz2,0,0,[],[])
    if len(Matriz1[0])==len(Matriz2[0]):
        if isinstance(Matriz1[0],list) and isinstance(Matriz2[0],list):
            if isinstance(Matriz1[0][0],int) and isinstance(Matriz2[0][0],int):
                return aux_mult_matrices(Matriz1,Matriz2,0,0,0,[])
            else:
                return "error."
        else:
            return "error."
    else:
        return "error"
            
def aux_mult_matrices(vec,matriz,i,j,esc,final):
    if i==len(matriz):
        return final
    else:
        while j<len(matriz[0]):
            escalar=vec[0][j]*matriz[i][j]
            esc=esc+escalar
            j+=1
        final=final+[esc]
        return aux_mult_matrices(vec,matriz,i+1,0,0,final)

def transpuesta(Matriz,i,j,tmp,Final):
    if j<len(Matriz[0]):
        while i<len(Matriz):
            tmp=tmp+[Matriz[i][j]]
            i+=1
        j+=1
        Final=Final+[tmp]
        return transpuesta(Matriz,0,j,[],Final)
    else:
        return Final
            
            
    
        

