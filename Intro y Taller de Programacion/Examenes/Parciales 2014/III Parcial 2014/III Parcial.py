#Saca la nota final de los estudiantes

def nota_fin(VecDistNot, MatNotObt, MatTotNot):
    if isinstance(MatNotObt,list) and isinstance(MatNotObt[0],list):
        if isinstance(VecDistNot,list):
            if len(VecDistNot)==5:
                return aux_nota(VecDistNot,MatNotObt,MatTotNot,0)
            else:
                return "Valores invalidos."
        else:
            return" Error."
    else:
        return "Error2."

def aux_nota(Vec,MatNotas,Matfinal,i):
    if len(MatNotas)==len(Matfinal):
        return Matfinal
    else:
        notafinal=mult_vxm(Vec,MatNotas[i][1:],0)
        if notafinal in range(1,100) or notafinal<=100 :
            vectemp=[MatNotas[i][0],notafinal]
            Matfinal.append(vectemp)
            return aux_nota(Vec,MatNotas,Matfinal,i+1)

def mult_vxm(Vec,VNotas,result):
    if len(Vec)==len(VNotas):
        if Vec==[]:
            return result
        else:
            multi= Vec[0]*VNotas[0]
            result=result+multi
            return mult_vxm(Vec[1:],VNotas[1:],result)
        
                    
##["Pablo",70,100,70,70,80]
##["Esteban",90,100,70,70,75]

#Matriz Cuadrada Binaria

def valmovil(Mat1,Mat2):
    if isinstance(Mat1,list) and isinstance(Mat1[0],list):
        if isinstance(Mat2,list) and isinstance(Mat2[0],list):
            if len(Mat1)== len(Mat1[0])and  len(Mat2)==len(Mat2[0]):
                if len(Mat1)==len(Mat2):
                    M1=aux_bin(Mat1,0,0,[],[],0)
                    M2=aux_bin(Mat2,0,0,[],[],0)
                    return M1, M2
                else:
                    return "Tamaño incompatible en Matrices."
            else:
                return "La Matriz no es cuadrada."
        else:
            return "No es Matriz."
    else:
        return "No es Matriz."

def aux_bin(Mat1,i,j,fila,columna,cant1):
    if i>len(Mat1)-1:
        if cant1==1:
            tupla=tuple(fila+columna)
            return [True,tupla]
        elif cant1==0:
            return"No hay objeto presente en matriz."
        else:
            return"Aparece estela del objeto en matriz."
    else:
        if j<len(Mat1[0]):
            if Mat1[i][j]==0:
                return aux_bin(Mat1,i,j+1,fila,columna,cant1)
            elif Mat1[i][j]==1:
                return aux_bin(Mat1,i,j+1,fila+[i],columna+[j],cant1+1)
            else:
                return "Valor Invalido en Matriz."
        else:
            return aux_bin(Mat1,i+1,0,fila,columna,cant1)
#Cordenadas del movimiento del 1


def pasmovil(Mat1,Mat2):
    tupla=valmovil(Mat1,Mat2)
    M1=tupla[0][1]
    M2=tupla[1][1]
    M1=[M1[0],M1[1]]
    M2=[M2[0],M2[1]]
    return aux_pas(M1,M2,[])

def aux_pas(M1,M2,final):
    if M1[0]>M2[0]:
        final.append('S')
        M1[0]=M1[0]-1
        return aux_pas(M1,M2,final)
    elif M1[0]<M2[0]:
        final.append('N')
        M1[0]=M1[0]+1
        return aux_pas(M1,M2,final)
    else:
        if M1[1]>M2[1]:
            final.append('W')
            M1[1]=M1[1]-1
            return aux_pas(M1,M2,final)
        elif M1[1]<M2[1]:
            final.append('E')
            M1[1]=M1[1]+1
            return aux_pas(M1,M2,final)
        else:
            return final
    

            
            
            
            
    










                        
                        
            
        



    




