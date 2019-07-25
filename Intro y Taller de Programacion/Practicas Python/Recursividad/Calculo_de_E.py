"""
* * * * * * * * * * * * * * * * * * * * * * 
* The value of an exponential function    *
* base e. It is calculated using the      *
* taylor series. It uses stack recursion. *
* Input: 								  *
* 	- X: The number of the exponential.   *
*   - N: The number of iterations. 		  *
* Output:								  *
*	The result of the exponential .		  *
* Restrictions:							  *
*	- N is limited to the CPU  capacity.  * 
* * * * * * * * * * * * * * * * * * * * * *
 """
#Author: Pablo Garcia

#Calculates the factorial of a number.	
def fact(X):
    if X==0:
        return 1
    else:
        return X*fact(X-1)

#Main function to be called.
def cal_e(X,N):
    if N==0:
        return 1
    else:
        return aux_cal(X,N,1)

#
def aux_cal(X,N,I):
    if N<I:
        return 1
    else:
        formula= (X**N)/(fact(N))
        return formula+ aux_cal(X,N-1,I)