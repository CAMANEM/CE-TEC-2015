"""
*******************************************************************
        Instituto Tecnológico de Costa Rica

            Ingeniería en Computadores


 Lenguaje: Python 3.4.2
 Autor: Pablo Garcia Brenes 
 Versión: 1.1
 Fecha Última Modificación: Mayo 3/2015

Descripcion:
    - comp: Verifica si el numero del parametro 1 esta contenido
             en el parametro 2.
 
Entrada:
    - par1: Primer parametro.
    - par2: Segundo parametro.
Salida: 
    - comp: Un boolean que indica si lo contiene o no.

Restricciones:
    - Debe contener enteros en cada parametro.
 
******************************************************************* """

def comp (par1,par2):
    if isinstance(par1,int) and isinstance (par2,int):
        return aux(par1, par2,par2)
    else:
        return "Error, ingrese enteros."

def aux (par1,par2,copia):
    if par1==0:
        return True
    else:
        if par1%10==par2%10:
            return aux(par1//10,par2,copia)
        else:
            return verf(par1,par2//10,copia)

def verf(par1,par2,copia):
    if par2==0:
        return False
    else:
        menos= par1%10
        menos2= par2%10
        if menos== menos2:
            return aux(par1//10,copia,copia)
        else:
            return verf(par1,par2//10,copia) 




    
