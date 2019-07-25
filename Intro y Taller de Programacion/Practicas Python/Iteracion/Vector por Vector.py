#Multiplica Vectores con iteracion
def vecXvec(Vec1,Vec2,result):
    if isinstance(Vec1,list) and isinstance(Vec2,list):
        if len(Vec1)==len(Vec2):
            while Vec1!=[]:
                mult=Vec1[0]*Vec2[0]
                result=result+mult
                Vec1=Vec1[1:]
                Vec2=Vec2[1:]
            return result


#Multiplica Vectores con iteracion de for
def VecXVec(Vec1,Vec2,result):
    if isinstance(Vec1,list) and isinstance(Vec2,list):
        if len(Vec1)== len(Vec2):
            for i in range(0,len(Vec1)):
                if i <len(Vec1):
                    mult=Vec1[i]*Vec2[i]
                    result= result+mult
            return result
        
