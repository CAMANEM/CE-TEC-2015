"""
* * * * * * * * * * * * * * * * * * * * * 
* The value of an sin, it is calculated *
* using the taylor series. It uses tail *
* recursion.                            *
* Input:                                *
*   - X: Number to evaluate in radians. *
*   - N: The number of iterations.      *
* Output:                               *
*   The result of the sin.              *
* Restrictions:                         *
*   - N must be between 10 and 20.      * 
* * * * * * * * * * * * * * * * * * * * *
 """
 #Author: Pablo Garcia
 
def facto(N):
    if N==0:
        return 1
    else:
        return N*facto(N-1)

def Sen(X,N):
    if N in range (10,20) or N==20:
        return aux_sen(X,N,0)
    else:
        return "Numero debe estar entre 10 y 20"
    
def aux_sen(X,N,result):
    if N<0:
        return result
    else:
        formula=(((-1)**N)/(facto((2*N)+1)))*(X**((2*N)+1))
        return aux_sen(X,N-1,result+formula)

print(Sen(3.14,20))