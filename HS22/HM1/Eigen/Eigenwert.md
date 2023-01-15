Ein Eigenwert (auch Eigenvalue genannt) ist ein Skalar, der die Veränderung einer Matrix beschreibt, wenn sie auf einen bestimmten Vektor angewendet wird. Ein Eigenraum ist die Menge aller Vektoren, die bei Anwendung der Matrix auf sie denselben Eigenwert ergeben.

Einfacher ausgedrückt: Ein Eigenwert ist ein spezieller Wert, der beschreibt, wie sich eine Matrix verändert, wenn man sie auf bestimmte Vektoren anwendet. Der Eigenraum ist die Menge aller Vektoren, die diesen Eigenwert ergeben.

$x^2+2x-3= 0$: $p=2$ und $q=3$

$$
x_{1,2} =
-
\frac{p}{2}
\pm
\sqrt{
\left(
\frac{p}{2}
\right)^2
-q
}
$$



## Charakteristische Form einer Matrix
```python
import numpy as np

# Beispielmatrix
A = np.array([
	[13, -4],
	[30, -9]
])

# Charakteristisches Polynom berechnen
p = np.poly(A)

# Polynom in erweiterte Form umwandeln
p = np.poly1d(p)

print (f"Charakteristische Form: {p}")
eigenvalues, eigenvectors = np.linalg.eig(A)

# Achtung -> Werte sind zu runden
print ("Eigenwerte", eigenvalues)
```

## Berechnen
- Nur möglich, wenn Matrix invertierbar ist.
$$
\left|
A - \lambda
\right|
=0
$$
```python
import numpy as np

# Define matrix
A = np.array([[2, 5], [-1, -2]])

# Calculate eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

# Select eigenvector for eigenvalue of interest

def normalize_vector(vector):
    vector_length = np.linalg.norm(vector)
    normalized_vector = vector / vector_length
    return normalized_vector

for eigenvalue in eigenvalues:
    eigenvector = eigenvectors[:,0]
    normed = normalize_vector(eigenvector).T
    
    
    # Define linear combination of eigenvectors
    alpha = 2
    beta = 3
    eigenplane = alpha * eigenvector.T + beta * eigenvector.T

    print("Für den Eigenwert:", round(eigenvalue,4))
#     
    print("Eigenplane:", eigenplane)
```