#Author: Pablo Garcia
def mult_matriz(matriz1,matriz2):
    if len(matriz1[0])==len(matriz2):
        tras=traspuesta(matriz2,[])
        return aux_mult(matriz1,tras,[])
    elif len(matriz2[0])==len(matriz1):
        tras=traspuesta(matriz1,[])
        return aux_mult(matriz2,tras,[])

def traspuesta(matriz,final):
    for j in range(0,len(matriz[0])):
        vec=[]
        for i in range(0,len(matriz)):
            vec.append(matriz[i][j])
        final.append(vec)
    return final

def aux_mult(matriz1,matriz2,final):
    for i in range(0,len(matriz1)):
        temp=[]
        for j in range(0,len(matriz2)):
            esc=mult_vec(matriz1[i],matriz2[j],0)
            temp.append(esc)
        final.append(temp)
    return final


def mult_vec(Vec1,Vec2,escalar):
    esc=0
    for i in range(0,len(Vec1)):
        esc= (Vec1[i]*Vec2[i])
        escalar=escalar+esc
    return escalar
        
