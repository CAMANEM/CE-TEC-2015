#Multiplicacion de Matriz

def mult_mat(Mat1,Mat2):
    if isinstance(Mat1,list) and isinstance(Mat2,list):
        if len(Mat1)==len(Mat2):
            nuevM2= traspuesta(Mat2) #Saca traspuesta a la M2 para facilitar multiplicacion
            return aux_mult(Mat1,nuevM2,0,[],[])
        else:
            return "Fatality."
    else:
        return "K.O"
#Saca la transpuesta de la Matriz 2
def traspuesta(Matriz):
    return traspuesta_aux(Matriz,0,len(Matriz)-1,[],[])

def traspuesta_aux(Matriz,I,filas,vectemp,Res):
    if I>filas:
        Res.append(vectemp)
        return traspuesta_aux(Matriz,0,filas,[],Res)
    elif Matriz[filas]==[]:
        return Res
    else:
        vectemp.append(Matriz[I][0])
        Matriz[I]=Matriz[I][1:]
        return traspuesta_aux(Matriz,I+1,filas,vectemp,Res)


#Funcion auxiliar de la multiplicacion
def aux_mult(Mat1,Mat2,J,vectemp,final):
    if Mat1==[]:
        return final
    else:
        if J<len(Mat1[0]): #Verifica
            Vec=mult_vec(Mat1[0],Mat2[J],0)
            vectemp.append(Vec)
            return aux_mult(Mat1,Mat2,J+1,vectemp,final)
        else:
            final.append(vectemp)
            return aux_mult(Mat1[1:],Mat2,0,[],final)

#Multiplica cada Vector (Fila1) por Vectors de matriz 2

def mult_vec(Vec1,Vec2,result):
    if len(Vec1)==len(Vec2):
        if Vec1==[]:
            return result
        else:
            mult=Vec1[0]*Vec2[0]
            result=result+mult
            return mult_vec(Vec1[1:],Vec2[1:],result)
    else:
        return "No es una matriz valida."
        
##
##[1,2,3]    [2,3,5]
##[4,5,6] X  [5,7,9] 
##[7,8,9]    [2,4,7]
##
##
##[2,5,2]
##[3,7,9]
##[5,9,7]
##
##
##len(Mat2)<indice
##matriznuvea.append(Mat2[i][indice])

