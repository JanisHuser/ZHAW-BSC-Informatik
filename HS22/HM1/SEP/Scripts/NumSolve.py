import numpy as np
import matplotlib
from numbers import Number

class GaussCalc():

    def __init__(self, a: np.array, b: np.array, log: bool = True):
        self._rows, self._columns = a.shape

        self._matrix: np.array = np.append(a, b, axis=1)
        self._pivoting = True
        self._log = log

    def set_pivoting(self, enable: bool) -> None:
        self._pivoting = enable
        
    def calc(self):
        
        
        print (f"Starting Matrix \n{self._matrix}")
        
        for i in range(self._rows):
            
            if self._log:
                print (f"\ncurrent row: {i}")

            if self._matrix[i][i] == 0.0:
                if self._log:
                    print ("switch row", end='')
                self.switch_row(i)
            else:
                if self._log:
                    print ("apply gauss")
                self.apply_gauss(i)
                
                
            print (f"Matrix: \n{self._matrix}")

        if self._pivoting == False:
            return self._matrix

        return self.reverse_substitution()


    def switch_row(self, row: Number) -> None:
        for i in range(row+1, self._rows):
            cell = self._matrix[i][row]

            if cell != 0.0:
                # Switch Row
                print (f" with {i}")
                temp = self._matrix[row]
                self._matrix[row] = self._matrix[i]
                self._matrix[i] = temp

                return

        raise Exception("No rows available anymore")

    def apply_gauss(self, row: Number) -> None:

        top_left_cell = self._matrix[row][row]

        for i in range(row+1, self._rows):
            ratio = self._matrix[i][row] / top_left_cell

            for j in range(self._columns+1):
                self._matrix[i][j] = self._matrix[i][j] - ratio * self._matrix[row][j]

    def reverse_substitution(self) -> None:
        x = np.zeros(self._rows)

        n = self._rows

        x [n -1] = self._matrix[n-1][n] / self._matrix [n-1][n-1]

        for i in range (n-2, -1, -1):
            x[i] = self._matrix[i][n]

            for j in range(i+1, n):
                x[i] = x[i] - self._matrix[i][j] * x[j]

            x[i] = x[i] / self._matrix[i][i]

        return x
    


def calc_gauss(a: np.array, b: np.array, log: bool = True):
    gauss = GaussCalc(a, b, log)
    gauss.set_pivoting(False)

    return gauss.calc()
    
    
def calc_qr(A: np.array):
    A = np.copy(A)  # necessary to prevent changes in the original matrix A_in
    
    A = A.astype('float64')  # change to float

    n, cols = np.shape(A)

    if n != cols:
        raise Exception('Matrix is not square')

    Q = np.eye(n)
    R = A

    for j in np.arange(0, n - 1):
        a = np.copy(R[j:, j]).reshape(n - j, 1)
        e = np.eye(n - j)[:, 0].reshape(n - j, 1)
        length_a = np.linalg.norm(a)
        sig = 1 if a[0] >= 0 else -1

        v = a + sig * length_a * e
        u = 1 / np.linalg.norm(v) * v
        H = np.eye(n - j) - 2 * u * np.transpose(u)

        Qi = np.eye(n)
        Qi[j:, j:] = H

        R = np.dot(Qi, R)
        Q = np.dot(Q, np.transpose(Qi))
        
    return (np.round(Q, 4), np.round(R, 4))