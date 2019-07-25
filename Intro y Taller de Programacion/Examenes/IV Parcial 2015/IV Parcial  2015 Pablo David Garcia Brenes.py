"""
*********************************************************************
		Instituto Tecnológico de Costa Rica

		    Ingeniería en Computadores


Lenguaje: Python 3.4.2
Autor: Pablo David Garcia Brenes
Versión: 1.0
Fecha Última Modificación: Junio 10/2015
Carne:2015083681

Profesor: Milton Villegas Lemus
Curso: Introduccion a la Programacion

IV Parcial
 
*********************************************************************** """

#============================ 1 ================================================#
def nuev_bool(Matriz):
    if len(Matriz)==len(Matriz[0]):
        base10= verif(Matriz,0,True)#Agregue parametro
        if base10==True:
            return aux_bool(Matriz,0,[])
        else:
            return "No son numeros enteros base 10."
    else:
        return "No es una matriz cuadrada."

def verif(Mat,j,entero):
    for i in range(0,len(Mat)):
        j=0  #agregue esto
        while j<=len(Mat)-1:
            if isinstance(Mat[i][j],int): #puse el isinstance
                j+=1
            else:
                entero= False
                j+=1
    return entero

def aux_bool(Matriz,temp,final):
    for i in range(0,len(Matriz)):
        vec=[]
        for j in range(0,len(Matriz[0])):
            string=str(Matriz[i][j])
            temp=0 #Se agrego esto
            for n in range(0,len(string)):
                num=int(string[n])
                temp=temp+num
            if temp%3==0:
                vec.append('True')
            elif temp%3!=0:
                vec.append('False')
        final.append(vec)
    return final

#nuev_bool([[123,34,7],[54,67,98],[4563,15,76]])
#================================== 2 ===============================#

def reloj_arena_hor(Matriz):
    if len(Matriz)==len(Matriz[0]):
        return aux_reloj(Matriz,0,len(Matriz)-1,[])
    else:
        return " Error: Verifique que la matriz de entrada sea cuadrada."

def aux_reloj(Mat,i,n,final):
    j=n
    vec=[]
    while j>=0:
        if Mat[j][n]<0:
            vec.append(Mat[j][n])
            j-=1
        else:
            j-=1
    j=1
    p=n-1
    while j<=n:
        if Mat[j][p]<0:
            vec.append(Mat[j][p])
            j+=1
            p-=1
        else:
            j+=1
            p-=1
    j=n-1#se agrego -1
    while j>=0:
        if Mat[j][i]<0:
            vec.append(Mat[j][i])
            j-=1
        else:
            j-=1
    i=1
    while i<n:
        if Mat[i][i]<0:
            vec.append(Mat[i][i])
            i+=1
        else:
            i+=1
    final+=vec
    if final==[]: #Se agrego este if 
        return "No hay numeros negativos dentro del recorrido de la matriz."
    else:
        return final
    
#reloj_arena_hor([[-2,3,1,6],[-1,0,-7,-5],[-9,8,-1,6],[-6,-2,-4,1]])
    
#===================== 4 ======================================#
def mxnbin(M,N):
    if len(M[0])==len(N):
        tras=traspuesta(N,[])
        return aux_mult(M,tras,[])
    else:
        return "Las matrices no tienen las dimensiones adecuadas."

def traspuesta(N,trasp):
    for j in range(0,len(N[0])): #agregue palabra len
        vector=[]
        for i in range(0,len(N)): #agregue palabra len
            vector.append(N[i][j])
        trasp.append(vector)
    return trasp

def aux_bin(mat1,matb):
    for i in range(0,len(mat1)):
        temp=[]
        for j in range(0,len(mat1[0])):
            if mat1[i][j]=="Uno":
                temp.append(1)
            elif mat1[i][j]=="Cero":
                temp.append(0)
            else:
                return "Error."
        matb.append(temp)
    return matb

def aux_mult(mat1,mat2,final):
    mat1=aux_bin(mat1,[])
    mat2=aux_bin(mat2,[])
    for i in range(0,len(mat1)):
        vec=[]
        for j in range(0,len(mat2)):
            esc=mult_vectores(mat1[i],mat2[j],0)
            vec.append(esc)
        final.append(vec)
    return [mat1,mat2,final]

def mult_vectores(V1,V2,escalar):
    for i in range(0,len(V1)):
        temp=V1[i]*V2[i]
        escalar= escalar+temp
    return escalar

#mxnbin([["Uno","Cero"],["Uno","Uno"],["Cero","Cero"]],[["Uno","Uno","Uno"],["Uno","Cero","Cero"]])
    
    
            


#============================== 3 ===================================#

class reloj:
    def __init__(self,Fabricante,Numeracion,Modelo): #Se agrego esta linea
        self.Fabricante=Fabricante
        self.Numeracion=Numeracion 
        self.Modelo=Modelo 
    def mostrar(self):
        print("Fabricante:" +(self.Fabricante)+" Numeracion:" +(self.Numeracion)+ " Modelo:"
          +(self.Modelo))
class Pulso(reloj):
    def __init__(self,Fabricante,Numeracion,Modelo,TipoBrazalete,Longitud,Duennos): #Se agrego esta linea
        reloj.__init__(self,Fabricante,Numeracion,Modelo)
        self.TipoBrazalete=TipoBrazalete #Cambie Hilera por TipoBrazalete
        self.Longitud=Longitud #Cambie num por Longiud
        self.Duennos=Duennos #Cambie lista por Duennos
    def mostrar(self):
        reloj.mostrar(self)#Se agrego
        print("TipoBrazalete:"+(self.TipoBrazalete)+" Longitud:"+(self.Longitud)+" Duennos:"+(self.Duennos))
    def cambiar_braz(self,Tipo,Long):
        self.TipoBrazalete=Tipo
        self.Longitud=Long
    def agregar_duenno(self,lista):
        self.Duennos+=lista
class Pared(reloj):
    def __init__(self,Fabricante,Numeracion,Modelo,TipoMueble,Material,Duennos): #Se agrego esta linea
        reloj.__init__(self,Fabricante,Numeracion,Modelo)
        self.TipoMueble=TipoMueble #Cambie variable
        self.Material=Material #Cambie variable
        self.Duennos=Duennos #Cambie variable
    def agregar_duenno(self,lista):
        self.Duennos+=lista
    def mostrar(self):
        reloj.mostrar(self) #Agregue linea
        print("TipoMueble:"+(self.TipoMueble)+" Material:"+(self.Material)+" Duennos:"+str(self.Duennos))
                       




