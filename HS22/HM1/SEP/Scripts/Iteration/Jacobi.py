import numpy as np
from numbers import Number

from .LinalgBase import LinalgBase


class Jacobi(LinalgBase):
    
    def __init__(self, A: np.array, b: np.array, x0: np.array):
        super().__init__(A, b, x0)
        
    def calc_B(self) -> np.array:
        [D, D_inv, L, R] = self.decomposite_A()
        B = np.dot(-1, D_inv.dot(np.add(L, R)))
        return B
        
    def calc_xn(self, x):
        [D, D_inv, L, R] = self.decomposite_A()
        B = self.calc_B()
        
        return np.add(B.dot(x), D_inv.dot(self._b))
        
    
        
    # Static Methods
    def create_A_diagonal(n, c) -> np.array:
        '''
        Creates a matrix of form
        c, -1, 0 ...
        -1, c, -1 ...
        0, -1, c, -1, ... (n)
        .
        (n)
        '''
        a = []
        for i in range(n):
            before = i-1
            
            for _ in range(before):
                a.append(0)
            
            if i > 0:
                a.append(-1)
            
            a.append(c)
            
            if i < (n-1):
                a.append(-1)
                
            for _ in range(n-before-3):
                a.append(0)

        return np.asarray(a, dtype='float64').reshape(n, int(len(a)/n))
        
    def create_b_diagonal(n, c):
        '''
        Creates a matrix of form
        c
        .
        .
        c
        '''
        b = np.zeros(n, dtype='float64')
        b[0] = c
        b[:1] = c
        return b 
 
           
        