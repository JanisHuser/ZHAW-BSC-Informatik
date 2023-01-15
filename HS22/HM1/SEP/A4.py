import numpy as np
from Scripts.NumSolve import calc_gauss


def Slow_LR(A):
    m,n = A.shape
    L = np.eye(n)
    R = A.astype('float64')


    for k in range(n-1):
        for j in range(k+1,n):
            L[j,k] = R[j,k]/R[k,k]
            for i in range(k,n):
                R[j,i] = R[j,i]-L[j,k]*R[k,i]
    return (L,R)


A = np.array([
    [1, 1, 1,],
    [2, 2, 5],
    [4, 6, 8]
])

print(Slow_LR(A))