#Suma de 2 matrices
#Suma un Vector (linea) a la vez

def suma_matriz(Mat1,Mat2):
    if len(Mat1)== len(Mat2) and len(Mat1[0])== len(Mat2[0]):
        return aux_sum(Mat1,Mat2,0,len(Mat1)-1,[])
    else:
        return "No tienen el mismo largo."

def aux_sum(Mat1,Mat2,i,filas,result):
    if i>filas:
        return result
    else:
        suma= sum_vec(Mat1[i],Mat2[i])
        result.append(suma)
        return aux_sum(Mat1,Mat2,i+1,filas,result)


def sum_vec(Vec1,Vec2):
    if isinstance (Vec1,list) and isinstance(Vec2, list):
        return aux_vec(Vec1,Vec2,[])
    else:
        return "Error: No son vectores validos."

def aux_vec(Vec1,Vec2,result):
    if Vec1==[]:
        return result
    else:
        if isinstance(Vec1[0],int):
            suma= Vec1[0]+Vec2[0]
            result.append(suma)
            return aux_vec(Vec1[1:],Vec2[1:],result)
        else:
            return "No son valores numericos."

            
                
                 
