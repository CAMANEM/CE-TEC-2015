import time
import random
import sys
sys.setrecursionlimit(20000)
    

def lista_rand(num,Sort): #Crea los numeros aleatoreamente
    if Sort in range(1,4): #1 es para BubbleSort, 2 para SelectionSort, 3 para QuickSort
        return aux_lista_rand(num,[],Sort)
    else:
        return "Sort debe ser 1 para BubbleSort, 2 Para Selection Sort, 3 Para Quick Sort."
    

def aux_lista_rand(num,lista,Sort):#Parametro la cantidad de elementos que debe tener la lista
    if num>=100: #Verifica que sean mas de 100 cifras lo deseado
        if len(lista)==num: #Ingresa la lista en el algoritmo de Ordenamiento
            if Sort==1:
                return BubbleSort(lista)
            elif Sort==2:
                return SeleccionSort(lista)
            else:
                return QuickSort(lista)
        else:
            x=random.randrange(0,100) #Genera numero random
            lista=lista+[x] #Concatena el numeroo
            return aux_lista_rand(num,lista,Sort)
    else:
        return "Error tienen que ser 100 numeros de 4 cifras cada uno."

#============================================================================#       
def BubbleSort(Lista):
    tiempo=time.time()
    return burbuja_aux(Lista, 0, 0, len(Lista)-1, False), time.time()-tiempo #Llamada a funcion auxiliar

def burbuja_aux(lista, i, j, n, Flag):
    if i>n: #Condicion de finalizacion
        return lista+[tiempo+time.time()]#Retorna la lista final
        
    elif j> n - i - 1: #Compara j con el ultimo elmento 
        if Flag==True: #Para saber cuando debe incrementar i
            return burbuja_aux(lista, i + 1, 0, n, False,) #Incrementa i para compara
        else:
            return lista
    elif lista[j] > lista[j + 1]: #Compara elemento con siguiente elmento de la lista
        tmp = lista[j] #Guarda temporalmente el elmento que va a remplazar
        lista[j] = lista[j + 1] #mueve el num mayor hacia adelante
        lista[j + 1] = tmp #Ingrese el num gruadado (menor) un espacio atras
        return burbuja_aux(lista, i, j + 1, n, True,) #Es para incrementar i
    else:
        return burbuja_aux(lista, i, j + 1, n, Flag)
    

#=============================================================#
def SeleccionSort(lista):
    tiempo=time.time()
    return seleccion_aux(lista, 0, len(lista)-1), time.time()-tiempo
def seleccion_aux(lista, i, largo):
    if i>=largo: #Condicion de finalizacion
        return lista
    else:
        menor= NumMenor(lista, i, i) #Llama funcion que obtiene el numero menor
        temp= lista[i]#Guarda el numero mayor
        lista[i]=lista[menor] #Pone numero menor antes de su posicion anterior
        lista[menor]=temp #Pone numero mayor un indice mas adelante
        return seleccion_aux(lista,i+1,largo,) #Aumenta indice
def NumMenor(lista,i, num): #Funcion que saca el numero menor
    if i>=len(lista)-1: #Condicion de finalizacion
        return num #retorna el numero menor
    else:
        if lista[num]>lista[i+1]: #Compara los numeros
            return NumMenor(lista,i+1,i+1)
        else:
            return NumMenor(lista,i+1,num)
#===============================================================#
def QuickSort(Lista):
    tiempo= time.time()#Para el tiempo
    return aux_QuickSort(Lista), time.time()-tiempo
def aux_QuickSort(Lista):
    NumMenores = [] #Crea listas vacias para guardar los nums correspondientes
    NumIguales = []
    NumMayores = []
    if len(Lista) <= 1: #Cuando ya haya recorrido todo retona la lista
        return Lista
    Pivote = Lista[-1] #Comienza el Pivote en el ultimo elemento
    partir(Lista, 0, len(Lista), Pivote, NumMenores, NumIguales, NumMayores)#Parte la lista 
    retornar = aux_QuickSort(NumMenores)#Llamada recursiva pero solo con la lista de los menores
    retornar.extend(NumIguales)#Adjunta los numeros iguales
    retornar.extend(aux_QuickSort(NumMayores)) #Llamada recursiva pero con lista de los mayores y los adjunta al terminar
    return retornar #Retorna la lista ordenada
def partir(Lista, i, n, Pivote, NumMenores, NumIguales, NumMayores):
    if i == n:
        return NumMenores, NumIguales, NumMayores
    if Lista[i] < Pivote: #Guarda los numeros menores al Pivote
        NumMenores.append(Lista[i])
    elif Lista[i] > Pivote: #Guarda los numeros mayores al Pivote
        NumMayores.append(Lista[i])
    elif Lista[i] == Pivote: #Guarda los numeros iguales al Pivote
        NumIguales.append(Lista[i])
    return partir(Lista, i + 1, n, Pivote, NumMenores, NumIguales, NumMayores)





"""
Operaciones sobre Secuencias:
x in s Ture si un item de s es igual a x, sino es False:
s=[1,2,3,4,5,6,7]
>>> 1 in s
True

x not in s True si ningun item de s es igual a x, sino False
>>> d=[1,2,3,7,7,7,7]
>>> 8 not in d
True

s + t Concatenacion de s y t
>>> sa=[1,3,3,8,7,7,7]
>>> as=[454,84,32,7,8,4,2]
>>> sa+sa
[1, 3, 3, 8, 7, 7, 7, 454, 84, 32, 7, 8, 4, 2]

s*n, n*s n copias de s concatenado:
>>> Lista=[50,20]
>>> b*3
[50, 20, 50, 20, 50, 20]

s[i:j] slice de s desde i hasta j
>>> ab=[1,2,3,4,7,27,6]
>>> ab[2:5]
[3, 4, 7]

s[i:j:k] slice desde i hasta j con salto en k
>>> b=[0,33,33,33,33,56,16,59,73,46,15]
>>> b[1:6:2]
[33, 33, 56]

mins(s) menor item de s:
>>> a=[4546,84,32,7,8,4,2]
>>> min(a)
2

max(s) mayor item de s:
>>>Listas=[2, 4, 8, 7, 32, 84, 4546]
>>>max(Listas)
4546

Operacion sovre secuencias Mutables:

s[i] = x item i de la secuencia s es reemplazado por x.
>>>c=[1, 5, 1, 2, 1, 2, 7, 34, 76, 1, 34, 55]
>>> a[2:6]=[8,0,8,0]
>>> a
[1, 5, 8, 0, 8, 0, 7, 34, 76, 1, 34, 55]



s[i:j] = t slice de s desde posición i a la j es reemplazada por el contenido del iterable t.
>>> abc=[12,3,46,3,46,1,36]
>>> abc[0:3]=[45]
>>> abc
[45, 3, 46, 1, 36]

del s[i:j] elimina los item en s desde i hasta j
>>> abcd=[12,3,46,3,46,1,36,2341,54]
>>> del abcd[0:3]
>>> abcd
[3, 46, 1, 36, 2341, 54]

s[i:j:k] = t Los elementos de s[i:j:k] son reemplazados por t
>>> e=[12,3,46,3,46,1,36,23]
>>> e[0:3:4]=[14]
>>> e
[14, 3, 46, 3, 46, 1, 36, 23]

del s[i:j:k] elimina los elementos s[i:j:k] de la lista
>>> ef=[12,3,46,3,46,1,12,34,21,36,23]
>>> del ef [2:3:5]
>>> ef
[12, 3, 3, 46, 1, 12, 34, 21, 36, 23]

s.append(x) agrega el elmento x al final de la lista s
>>> lis=[2,3,4]
>>> lis.append(1)
>>> lis
[2,3,4,1]

s.extend(x) concatena el elmento x al la lista s
>>> lisa=[12,3,4,6]
>>> lisa.extend([13])
>>> lisa
[12, 3, 4, 6, 13]

s.count(x) retorna el número de veces q x aparece en s
>>> lisad=[12,3,4,6,2,2,2,2]
>>> lisad.count(2)
4

s.index(x[, i[, j]]) retorna el menor k tal que s[k] == x and i <= k < j
>>> string1="Es un ejemplo del index."
>>> lista=[1,2,3,4,5,6,7,8,8,9,4,2]
>>> print(lista.index(3))
2

s.insert(i, x) Equivalente con i es la ubicacion donde desea insertar y x lo q desea insertar
>>>bas=[1,2,3,5,6,7,2,1,3,6,2,4]
>>> bas.insert(11,1234)
>>> bas
[1,2,3,5,6,7,2,1,3,6,2,4 1234]

s.pop(i) retorna s[i] de s pero tambien lo elimina de s al retornarlo
>>> sad=[12,3,4,6,2,23,1,4]
>>> sad.pop(6)
1
>>> sad
[12, 3, 4, 6, 2, 23, 4]

s.remove(x) elimina el elemento x de s
>>> rem=[6,5,4,3,2,1]
>>> rem.remove(2)
>>> rem
[6, 5, 4, 3, 1]

s.reverse() invierte los ítemes de s
>>> rev=[9,8,7,6,5,4,3,2,1]
>>> rev.reverse()
>>> rev
[1, 2, 3, 4, 5, 6, 7, 8, 9]

s.sort([key[,reverse]]) ordena los ítemes de s
>>> s=[91,23,15,20,17,22,14,26,18,21]
>>> s.sort(key=None,reverse=False)
>>> s
[14, 15,17,18,20,21,22,23,26,91] la ordena de menor a mayor
>>> s.sort(key=None,reverse=True)
>>> s
[91, 26, 23, 22, 21, 20, 18, 17, 15, 14] la ordena de menor a mayot por el reverse=True
"""


