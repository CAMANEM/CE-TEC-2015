def flat(lista, final):
    if lista==[]:
        return final
    else:
        if isinstance(lista[0],list)==False:
            return flat(lista[1:],final+[lista[0]])
        else:
            if isinstance(lista[0],list):
                nueva= lista.insert(0,lista[0])
                fin= nueva[1:]
                return flat(fin,final)
            else:
                return "hola"



def flats(lista):
    intostr= str(lista)
    newstr= intostr.replace("[", "")
    nuevstr= newstr.replace("]", "")
    string= nuevstr
    #nuevlista=list(nuevstr)
    return aux(string,[])
def aux(nuevstr,listafinal):
    if nuevstr==[]:
        return listafinal
    else:
        if nuevstr=="" or nuevstr[0]==" " or nuevstr[0]=="'":
            return aux(nuevstr[1:],listafinal)
        else:
            return aux(nuevstr[1:], listafinal+ [nuevstr[0]])
            
















Respuesta=[]
def comoYoLoHaria(lista):
    if lista!=[]:
        if isinstance(lista[0],list):
            comoYoLoHaria(lista[0])
            comoYoLoHaria(lista[1:])
        else:
            Respuesta.append(lista[0])
            return comoYoLoHaria(lista[1:])

