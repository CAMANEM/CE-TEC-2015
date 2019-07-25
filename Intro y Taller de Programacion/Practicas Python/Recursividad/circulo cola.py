from math import *
def circulo(Radio,cantip):
    cant=360//cantip
    return aux_circulo(Radio,0,cant,1,[])

def aux_circulo(Radio,angulo,anguloA,card,resp):
    if card>4:
        return resp
    else:
        if angulo>=90:
            return aux_circulo(Radio,0,anguloA,card+1,resp)
        else:
            if card==1:
                X=cos(angulo)*Radio
                Y=sin(angulo)*Radio
                lista=[[X,Y]]
                return aux_circulo(Radio,angulo+anguloA,anguloA,card,resp+lista)
            elif card==2:
                Y=cos(angulo)*Radio
                X=sin(angulo)*Radio
                lista=[[-X,Y]]
                return aux_circulo(Radio,angulo+anguloA,anguloA,card,resp+lista)
            elif card==3:
                X=cos(angulo)*Radio
                Y=sin(angulo)*Radio
                lista=[[-X,-Y]]
                return aux_circulo(Radio,angulo+anguloA,anguloA,card,resp+lista)
            elif card==4:
                Y=cos(angulo)*Radio
                X=sin(angulo)*Radio
                lista=[[X,-Y]]
                return aux_circulo(Radio,angulo+anguloA,anguloA,card,resp+lista)