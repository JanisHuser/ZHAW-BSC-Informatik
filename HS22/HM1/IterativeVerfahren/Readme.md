# Iterative Verfahren

- [Jacobi Verfahren](Jacobi.md)
- [Gauss-Seidel](Gauss-Seidel.md)
- [Konvergenz & Fehlerabschätzungen](Konvergenz.md)

```python,edtiable
import numpy as np
from enum import Enum
from typing import List, Tuple
from numbers import Number

class IterativeMethod(Enum):
    JACOBI = 1
    GAUSS_SEIDEL = 2
    
class IterativeCalc():
    def __init__(self, A: np.array, b: np.array, x0: np.array, tolerance: Number):
        self._A = A
        self._b = b
        self._x = [x0]
        self._tolerance = tolerance
        self._method: IterativeMethod = IterativeMethod.JACOBI
            
        # Do some magic
        [D, D_inv, L, U] = self.decomposite_A()
        self._D = D
        self._D_inv = D_inv
        self._L = L
        self._U = U
        
        self._calculate_xn = None
    
    # Sets the calculation method 
    def set_method(self, method: IterativeMethod) -> None:
        self._method = method
        if self._method == IterativeMethod.JACOBI:
            B = np.dot(-1, self._D_inv.dot(np.add(self._L, self._U)))
            
            def calculate_xn(x):
                return np.add(self._B.dot(x), self._D_inv.dot(self._b))
            
            self._calculate_xn = calculate_xn
        else:
            B = np.dot(-1, np.linalg.inv(np.add(self._D, self._L)).dot(self._U))
            
            def calculate_xn(self,x):
                return np.add(self._B.dot(x), np.linalg.inv(np.add(self._D, self._L)).dot(self._b))
            
            self._calculate_xn = calculate_xn
        
        self._B = B
        
    # Mittels a-priori die geschätzten Iterationen,
    # um die Toleranz tol zu erreichen, berechnen
    def estimate_iteration(self):
        x1 = self._calculate_xn(self._x[0])
        
        B_norm = np.linalg.norm(self._B, np.inf)
        x_norm = np.linalg.norm(x1 - self._x[0], np.inf)
        n = np.log(((1 - B_norm) / x_norm) * self._tolerance) / np.log(B_norm)
        return n
    
    # Mittels a-posteriori die Fehlerabschätzung
    # von x und x+1 berechnen
    def calc_error(self, x, xn):
        B_norm = np.linalg.norm(self._B, np.inf)
        x_norm = np.linalg.norm(xn - x, np.inf)

        err = (B_norm / (1 - B_norm)) * x_norm

        return err
    
    def calc(self):
        iteration = 0
        while True:
            x = self._x[iteration]
            xn = self._calculate_xn(x)
            
            self._x.append(xn)
            
            iteration += 1
            if self.calc_error(x, xn) <= self._tolerance:
                break
            else:
                x = xn

        return (xn, iteration)
    
    # Helper Methods
    def decomposite_A(self):
        D = np.diag(np.diag(self._A))
        D_inv = np.linalg.inv(D)
        L = np.tril(A, -1)
        R = np.triu(A, 1)

        return (D, D_inv, L, R)
    
    def get_xn(self, n: Number) -> np.array:
        if n > len(self._x):
            return False
        
        return self._x[n]
       
## SET YOUR STUFF HERE
A = np.array([[4, -1, 1],
                  [-2, 5, 1],
                  [1, -2, 5]])

b = np.array([[5, 11, 12]]).reshape(3, 1)
x = np.array([[0, 0, 0]]).reshape(3, 1)
tolerance = 1e-4

method = IterativeCalc(A, b, x, tolerance)
method.set_method(IterativeMethod.JACOBI)
result, iterations = method.calc()

## Set precision to 4
np.set_printoptions(precision=4)

print (f"Estimated iterations: {method.estimate_iteration()}")
print(f"Result after {iterations} iterations \n {result}")

n = 1
print (f"Result at x^{n}: \n {method.get_xn(n)}")
```
