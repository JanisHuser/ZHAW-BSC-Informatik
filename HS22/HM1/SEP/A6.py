# Aufgabe 6
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

        def is_abbruch():
            if k == 0:
                return False
            
            norm = np.linalg.norm(get_ev(k) - get_ev(k-1), 2)
            
            return norm <= tolerance

        while not is_abbruch():
            Av = A.dot(get_ev(k))
            v = Av / np.linalg.norm(Av)
    
            ev = eigenvalue(A, v)
            
            k += 1
            values.append((v, ev))
            
            if self._log:
                print(f"{k}\t{v.flatten()}\t{ev}")
            
            if np.abs(get_ew(k-1) - ev) < tolerance:
                break
        
            
        return values

# Define matrix
A = np.array([
    [3, 0, 0],
    [1, 3, 0],
    [0, 0, 6]
])

# Anfangsvektor
x = np.array([1, 1, 1])

mises_iteration = MisesIteration(A, x)

# Logging einstellen
mises_iteration.enable_log(False)

# Iteriere bis Differenz 0.01 getroffen
values = mises_iteration.iterate(10**(-15))

print ("Aufgabe 6")
print ("Teil b")
print ("=============== RESULTAT ===============")
print ("Eigenwert", round(values[len(values)-1][1], 5))
print ("Eigenvektor", values[len(values)-1][0].flatten())