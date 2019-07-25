
def cuadrado_matriz(matriz):
    if isinstance(matriz,list)and isinstance(matriz[0][0],str):
        if verf(matriz)==True:
            return aux_cuadrado(matriz,1,len(matriz)-1,[])
    else:
        return "error"

def verf(matriz):
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[0])):
            if matriz[i][j]=="A":
                pass
            elif matriz[i][j]=="B":
                pass
            elif matriz[i][j]=="C":
                pass
            elif matriz[i][j]=="D":
                pass
            elif matriz[i][j]=="E":
                pass
            elif matriz[i][j]=="F":
                pass
            elif matriz[i][j]=="1":
                pass
            elif matriz[i][j]=="2":
                pass
            elif matriz[i][j]=="3":
                pass
            elif matriz[i][j]=="4":
                pass
            elif matriz[i][j]=="5":
                pass
            elif matriz[i][j]=="6":
                pass
            elif matriz[i][j]=="7":
                pass
            elif matriz[i][j]=="8":
                pass
            elif matriz[i][j]=="9":
                pass
            elif matriz[i][j]=="0":
                pass
            elif matriz[i][j][0]=="-":
                pass
            else:
                return False
    return True

def aux_cuadrado(matriz,i,n,final):
    j=n
    temp=[]
    arriba=[]
    arr=[]
    abaj=[]
    while j>=0:
        if matriz[n][j][0]=="-":
            temp.append(matriz[n][j])
        while i<=n:
            if matriz[0][i][0]=="-":
                arriba.append(matriz[0][i])
            i+=1
        j-=1
    n=len(matriz)-2
    m=1
    while n>=0:
        if matriz[n][0][0]=="-":
            arr.append(matriz[n][0])
        n-=1
        while m<=len(matriz)-1:
            if matriz[m][len(matriz[0])-1][0]=="-":
                abaj.append(matriz[m][len(matriz[0])-1])
            m+=1
    final=temp+arr+arriba+abaj
    return final
                   
    
            
                

                       
                       
    
