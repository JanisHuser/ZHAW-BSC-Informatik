
import numpy as np

def is_orthogonal(q: np.array):
    qt = q.transpose()
    i = np.dot(q, qt)
    
    
    for j in range(i.shape[0]):
        if not i[j][j] == 1.0:
            return False
        
    return True
    