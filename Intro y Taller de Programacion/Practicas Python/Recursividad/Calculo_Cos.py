"""
* * * * * * * * * * * * * * * * * * * * * * 
* The value of an cos, it is calculated   *
* using the taylor series. It uses stack  *
* recursion.                              *
* Input:                                  *
*   - X: Number to evaluate in radians.   *
*   - N: The number of iterations.        *
* Output:                                 *
*   The result of the cos.                *
* Restrictions:                           *
*   - N must be between 10 and 20.        * 
* * * * * * * * * * * * * * * * * * * * * *
 """
#Author: Pablo Garcia

def Cos(X,N):
    if N in range (10,20) or N==20:
        return aux_cos(X,N,1)
    else:
        return "Numero debe estar entre 10 y 20"

def facto(N):
    if N<=1:
        return 1
    else:
        return N*facto(N-1)

def aux_cos(X,N,I):
    if N<I:
        return 1
    else:
        formula=(((-1)**N)/(facto(2*N)))* (X**(2*N))
        return formula + aux_cos(X,N-1,I)

print(Cos(3.14/4,20))