import numpy as np
from numbers import Number


class LinalgBase():
    def __init__(self, A, b, x0):
        self._A = A
        self._b = b
        self._x = [x0]
    
    def x_len(self) -> Number:
        return len(self._x)
        
    def get_x(self, index: Number) -> np.array:
        return self._x[index]
        
    def decomposite_A(self):
        '''
        Create decomposite of A
        returns [D, D_inv, L, R]
        '''
        D = np.diag(np.diag(self._A))
        D_inv = np.linalg.inv(D)
        L = np.tril(self._A, -1)
        R = np.triu(self._A, 1)

        return [D, D_inv, L, R]
        
    def calc_B(self) -> np.array:
        raise NotImplementedError()
        
    def calc_xn(self, x):
        raise NotImplementedError()
        
    def calc_a_posteriori_error(self,B, x, xn) -> Number:
        B_norm = np.linalg.norm(B, np.inf)
        x_norm = np.linalg.norm(xn - x, np.inf)

        err = (B_norm / (1 - B_norm)) * x_norm

        return err
        
    def estimate_a_priori(self, tol) -> Number:
        
        x0 = self._x[0]
        x1 = self.calc_xn(x0)
        
        B = self.calc_B()
        B_norm = np.linalg.norm(B, np.inf)
        x_norm = np.linalg.norm(x1 - x0, np.inf)

        n = np.log(((1 - B_norm) / x_norm) * tol) / np.log(B_norm)

        return n
    
        
    def iterate_n(self, n, log: bool = False):
        B = self.calc_B()
        
        if log:
            print(f"{0}.Iteration")
            print(self._x[0])
        
        for i in range(n):
            
            x = self._x[i]
            xn = self.calc_xn(x)
            
            self._x.append(xn)
            
            err = self.calc_a_posteriori_error(B, x, xn)
            
            if log:
                print(f"{i+1}.Iteration")
                print(self._x[i+1])
                print(f"A posteriori: {err}")
                
            
        return x
        
        
    def iterate(self, tolerance=-1, log: bool = False):
        i = 0
        B = self.calc_B()
        
        if log:
            print(f"{i}.Iteration")
            print(self._x[i])
        
        while True:
            
            x = self._x[i]
            xn = self.calc_xn(x)
            self._x.append(xn)
            
            err = self.calc_a_posteriori_error(B, x, xn)
            i += 1
            
            if log:
                print(f"{i}.Iteration")
                print(self._x[i])
                print(f"A posteriori: {err}")
            
            if err <= tolerance:
                break
            
        
        return x
    
