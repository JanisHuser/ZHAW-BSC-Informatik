import numpy as np
from numbers import Number

from .LinalgBase import LinalgBase


class GaussSeidel(LinalgBase):
    
    def __init__(self, A: np.array, b: np.array, x0: np.array):
        super().__init__(A, b, x0)
        
    def calc_B(self) -> np.array:
        [D, D_inv, L, R] = self.decomposite_A()
        B = np.dot(-1, np.linalg.inv(np.add(D, L)).dot(R))
    
        return B
        
    def calc_xn(self, x):
        [D, D_inv, L, R] = self.decomposite_A()
        B = self.calc_B()
        
        return np.add(B.dot(x), np.linalg.inv(np.add(D, L)).dot(self._b))