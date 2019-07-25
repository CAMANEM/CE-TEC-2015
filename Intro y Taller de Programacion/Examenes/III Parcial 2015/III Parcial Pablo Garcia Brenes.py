"""
*********************************************************************
		Instituto Tecnológico de Costa Rica

		    Ingeniería en Computadores


Lenguaje: Python 3.4.2
Autor: Pablo David Garcia Brenes
Versión: 2.0
Fecha Última Modificación: Mayo 22/2015
Carne:2015083681

Profesor: Milton Villegas Lemus
Curso: Introduccion a la Programacion

III Parcial
 
*********************************************************************** """
#Las entradas tienen que ser numeros en string 

def arena_hex(Matriz):   # Por problemas con la camara no pude documentar los cambio exactos ya que me faltaron unas fotos
    if isinstance(Matriz,list):
        return vali_arena(Matriz,Matriz)
    else:
        return "Error:no es matriz."

def vali_arena(M1,Mcopia):
    if M1==[]:  #Se les agrego estas dos lineas
        return aux_arena(Mcopia,0,0,len(Mcopia)-1,Mcopia)
    elif isinstance(M1[0],list) and isinstance(M1[0][0],str): #string str
        if len(Mcopia)==len(M1[0]):
            if M1==[]:
               return aux_arena(Mcopia,0,0,len(Mcopia)-1,Mcopia)
            else:
               return vali_arena(M1[1:],Mcopia)
        else:
            return "Error:Verifique que la matriz de entrada sea cuadrada."
    else:
        return "Ingrese los digitos en string."

def aux_arena(Mat,I,J,filas,Matcop): #Cambio en nombre de funcion
    if I>filas: #Se elimino una parte
        return atras(Matcop,[],len(Mat)-1,0,len(Mat[0])-1)
    elif J<=len(Mat[0])-1:#Se agrego =
        if len(Mat[I][J])!=1:
            if len(Mat[I][J])>2:
                     return "Hay numeros de mas de dos cifras en la matriz."
            else:
                if Mat[I][J][0]=="-":
                     return aux_arena(Mat,I,J+1,filas,Matcop)
                else:
                     return "Hay numeros de mas de dos cifras en la matriz."
        else:
            return aux_arena(Mat,I,J+1,filas,Matcop)
    elif I<=filas:                    #Se agrego =
        return aux_arena(Mat,I+1,0,filas,Matcop)

def atras(Matriz,neg,fila,J,columna):
    if columna<J:
        return diag(Matriz,neg,0,len(Matriz[0])-1,1,len(Matriz)-2)#cambio 0 por 1
    else:
        if Matriz[fila][columna][0]=="-":
            neg.append(Matriz[fila][columna])
            return atras(Matriz,neg,fila,J,columna-1)
        else:
            return atras(Matriz,neg,fila,J,columna-1)

def diag(Matriz,neg,I,columna,J,fila):
    if fila<I and J>columna:
        return atras1(Matriz,neg,0,0,len(Matriz[0])-2) #Cambie Mat por Matriz, -1 por -2, quite un len y puse 0
    else:
        if Matriz[fila][J][0]=="-":
            neg.append(Matriz[fila][J])
            return diag(Matriz,neg,I,columna,J+1,fila-1)
        else:
            return diag(Matriz,neg,I,columna,J+1,fila-1)

def atras1(Matriz,neg,fila,J,columna):
    if columna<J:
        return diag1(Matriz,neg,1,len(Matriz[0])-2,1,len(Matriz)-2)#Cambie -1 por -2
    else:
        if Matriz[fila][columna][0]=="-":
            neg.append(Matriz[fila][columna])
            return atras1(Matriz,neg,fila,J,columna-1)
        else:
            return atras1(Matriz,neg,fila,J,columna-1)

def diag1(Matriz,neg,I,columna,J,fila):
    if I>fila and J>columna: #Cambio boquita de I
        if neg==[]:
            return"No hay numeros negativos dentro del recorrido de la matriz."
        else:
            return neg
    else:
        if Matriz[fila][J][0]=="-":
            neg.append(Matriz[I][J])
            return diag1(Matriz,neg,I+1,columna,J+1,fila)
        else:
            return diag1(Matriz,neg,I+1,columna,J+1,fila)


# arena_hex([["-2","3","1","6"],["-1","0","-7","-5"],["-9","8","-1","-6"],["-B","-2","-4","1"]])
# arena_hex([["-2","3","1","6"],["-1","0","-7","-5"],["-9","8","-1","6"]])
#arena_hex([["3","1","C"],ArithmeticError["3","-1","3"],["3","1","2D"]])
#===========================================================================#

def multiplica_matrices(Mat1,Mat2):
    if isinstance(Mat1,list) and isinstance(Mat2,list):
        if isinstance(Mat1[0],list) and isinstance(Mat2[0],list): #M1 por Mat1
            if len(Mat1)==len(Mat2[0]):
                return traspuesta(Mat2,0,len(Mat2)-1,[],[],Mat1)
            elif len(Mat2)==len(Mat1[0]):
                return traspuesta(Mat1,0,len(Mat1)-1,[],[],Mat2)
            else:
                return "No es possible multiplicar las matrices."
        else:
            return "No es vector valido."
    else:
        return "No es matriz valido."

def traspuesta (M2,I,filas,vectemp,result,M1):
    if I>filas:
        result.append(vectemp)
        return traspuesta (M2,0,filas,[],result,M1)
    elif M2[filas]==[]:
        return multi_mat(M1,result,0,0,[],[])
    else:
        vectemp.append(M2[I][0])
        M2[I]=M2[I][1:] #Agreue linea
        return traspuesta(M2,I+1,filas,vectemp,result,M1) #Agregue la palabra traspuesta
                             
def multi_mat(M1,M2,I1,I2,vectmp,final):
    if I1>len(M1)-1:
        return final
    elif I2<=len(M2)-1:                #agregue =
        mult=mult_vec(M1[I1],M2[I2],0)
        vectmp.append(mult)
        return multi_mat(M1,M2,I1,I2+1,vectmp,final)
    elif I2>len(M2)-1:
        final.append(vectmp)
        return multi_mat(M1,M2,I1+1,0,[],final)   #vectemp pasa a []

def mult_vec(Vec1,Vec2,Res):
    if Vec1==[]:
        return Res
    else:
        if len(Vec1)==len(Vec2):
            mult=Vec1[0]*Vec2[0]
            Res=Res+mult
            return mult_vec(Vec1[1:],Vec2[1:],Res)
        else:
            return "Vectores no tienen misma dimension." # Se agrego este mensaje

#multiplica_matrices([[2,3,1],[9,6,3]],[[3,6,9],[0,4,7]])
#multiplica_matrices([[3,2,1],[0,1,1],[3,1,2]],[[2,2,2],[1,1,1],[3,0,3]])



#====================================================================================#

def resta_vector_c3(Vector1,Vector2):
    if isinstance(Vector1,list) and isinstance(Vector2,list):
        if len (Vector1)==len(Vector2):
            return aux_resta(Vector1,Vector2,[])
        else:
            return "Error: los vectores que desea restar tienen diferente dimension."
    else:
        return "Error: No son vectores."

def aux_resta(V1,V2,final):
    if V1==[]:
        return final
    elif V1[0] in range(0,3) or V1[0]==3:
        if V2[0] in range(0,3) or V2[0]==3:
            comple=comp(V2[0])
            if V1[0]==V2[0]:
                final.append(-3)
                return aux_resta(V1[1:],V2[1:],final)
            elif V2[0]==0:
                num=-(V1[0])
                final.append(num)
                return aux_resta(V1[1:],V2[1:],final)
            elif V1[0]>V2[0]:
                num=V1[0]+comple
                if num==5:
                    final.append(2)
                    return aux_resta(V1[1:],V2[1:],final)
                elif num==4:
                    final.append(1)
                    return aux_resta(V1[1:],V2[1:],final)
            elif V1[0]<V2[0]:
                num=V1[0]+comple
                if num==2:
                    final.append(-1)
                    return aux_resta(V1[1:],V2[1:],final)
                elif num==1:
                    final.append(-2)
                    return aux_resta(V1[1:],V2[1:],final)
                elif num==3:
                    final.append(-1)
                    return aux_resta(V1[1:],V2[1:],final)
        else:
            return "Error: La entrada no es un numero base cuatro valido." #Agregue los siguientes return 
    else:
            return "Error: La entrada no es un numero base cuatro valido."
        
def comp(num):
    comple=3-num
    return comple
            

#resta_vector_c3([0,3,2,3,9],[2,2,3,1,1])
#resta_vector_c3([2,2,3,1],[2,2,3,1,4])
#resta_vector_c3([1,2,3,2,3],[1,1,2,3,3,2])
#resta_vector_c3([1,3],[2,3,2])
#resta_vector_c3([3,1,0,2],[2,1,0,3])

