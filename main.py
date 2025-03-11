import numpy as np


#defining a fuction to perform gauss elimination
#A is the matrix of coefficients
#b is the vector of constants
def gauss_elimination(A,b):
    n = len(b)
    for i in range(n):
        #finding the maximum element in the column
        maxEl = abs(A[i][i])
        maxRow = i
        for k in range(i+1,n):
            if abs(A[k][i]) > maxEl:
                maxEl = abs(A[k][i])
                maxRow = k
        #swapping the maximum row with the current row
        for k in range(i,n):
            tmp = A[maxRow][k]
            A[maxRow][k] = A[i][k]
            A[i][k] = tmp
        tmp = b[maxRow]
        b[maxRow] = b[i]
        b[i] = tmp
        #making the elements below the diagonal zero
        for k in range(i+1,n):
            c = -A[k][i]/A[i][i]
            for j in range(i,n):
                if i == j:
                    A[k][j] = 0
                else:
                    A[k][j] += c * A[i][j]
            b[k] += c * b[i]
    #back substitution
    x = [0 for i in range(n)]
    for i in range(n-1,-1,-1):
        x[i] = b[i]/A[i][i]
        for k in range(i-1,-1,-1):
            b[k] -= A[k][i] * x[i]
    return x

#defining the matrix of coefficients

A = [[2,1,-1],[1,1,1],[1,-1,2]]
#defining the vector of constants
b = [2,3,3]
#calling the function
print(gauss_elimination(A,b))
#output : [1.0, 1.0, 1.0]
#This is the solution of the system of equations