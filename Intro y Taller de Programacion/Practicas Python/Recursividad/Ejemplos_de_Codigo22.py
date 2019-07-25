#Author: Fabian Solano
import math
def find_0(x):
        if isinstance(x,int):
                return find_0_aux(abs(x))
        else:
                return "Revise los datos ingresados"

def find_0_aux(x):
        if x == 0: #Condición de finalización 1
                return False
        else:
                if (x%10) == 0: #Condición de finalización 2
                        return True
                else:
                        return find_0(x//10)		


#palindromo


def palindromo(palabra):

        if isinstance(palabra,str):

                return palindromo_1

        else:

                return "Por favor ingrese una hilera"

def palindromo(palabra):

        if palabra == palabra[::-1]: # [begin:end: step] -1 reverses it as leavving rest in blank

                return True
        else:
                
                return False

#Factorial

def factorial(x):

        if isinstance(x,int):
                return factorial_aux(x)
        else:
                return "Ingrese un numero entero"
def factorial_aux(x):

        if x<1:
                return 1
        
        else:
                return x *factorial( x-1)


#Fibonacci

def fib(x):

        if isinstance(x,int):
                return fib_1(x)
        else:
                return "Por favor ingrese un numero entero"

def fib_1(x):

        if x==0 or x==1:

                return 1
        
        else:
                return fib_1(x-1)+fib(x-2)

#Octal a Decimal

def conv8(n):

        if isinstance(n,int):
                return conv(n)
        else:
                return "Por favor ingrese un numero entero"

def conv(n):
        if n == 0 or n<8:
                return n
        elif n>8:
              res= n%8
              return conv(n//8), res
