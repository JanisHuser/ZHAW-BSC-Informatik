import numpy as np
from numbers import Number

class MisesIteration():
    def __init__(self, A: np.array, v: np.array):
        '''
        A: np.array
        v: np.array (Startvektor)
        '''
        
        self._A = A
        self._v = v
        self._log = True
        
    def enable_log(self, log: bool) -> None:
        '''
        Enables logging in class
        '''
        self._log = log
        
    
        
    def iterate(self, tolerance: Number = 0.01):
        '''
        Gibt eine Liste mit dem Format (Eigenvektor, Eigenwert) zurück
        tolerance: Wiederhole iteration, solange Unterschied der Eigenwerte grösser ist
        '''
        values = []
            
        def get_ev(i):
            return values[i][0]
            
        def get_ew(i):
            return values[i][1]
        
        def eigenvalue(A, v):
            Av = A.dot(v)
            return v.dot(Av)
            
        A = self._A
        v = self._v
        k = 0
        
        ev = eigenvalue(A, v)
        
        values.append((v, ev))
        
        if self._log:
            print(f"k\tv^k\tλ^k")
            print(f"{k}\t{get_ev(k).flatten()}\t{round(get_ew(k),5)}\t")
        

        while True:
            Av = A.dot(get_ev(k))
            v = Av / np.linalg.norm(Av)
    
            ev = eigenvalue(A, v)
            
            k += 1
            values.append((v, ev))
            
            if self._log:
                print(f"{k}\t{v.flatten()}\t{round(ev,5)}")
            
            if np.abs(get_ew(k-1) - ev) < tolerance:
                break
        
            
        return values
            
        
    def iterate_n(self, n: Number):
        '''
        Gibt eine Liste mit dem Format (Eigenvektor, Eigenwert) zurück
        n: Anzahl iterationen
        '''
        
        values = []
            
        def get_ev(i):
            return values[i][0]
            
        def get_ew(i):
            return values[i][1]
        
        def eigenvalue(A, v):
            Av = A.dot(v)
            return v.dot(Av)
            
        A = self._A
        v = self._v
        
        ev = eigenvalue(A, v)
        
        values.append((v, ev))
        
        if self._log:
            print(f"k\tv^k\tλ^k")
            print(f"{0}\t{get_ev(0).flatten()}\t{round(get_ew(0),5)}\t")
        

        for k in range(n):
            Av = A.dot(get_ev(k))
            v = Av / np.linalg.norm(Av)
    
            ev = eigenvalue(A, v)
            
            values.append((v, ev))
            
            if self._log:
                print(f"{k+1}\t{v.flatten()}\t{round(ev,5)}")
        
            
        return values