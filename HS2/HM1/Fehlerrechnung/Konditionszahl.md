# Konditionszahl

```python,editable
import numpy as np

A = np.array([
	[1, 0, 2],
	[0, 1, 0],
	[1E-4, 0, 1E-4]
])

order = np.Infinity

A_norm = np.linalg.norm(A, order)

A_inv = np.linalg.inv(A)
A_inv_norm = np.linalg.norm(A_inverse, order)


print ("Normal")
print (A)
print ("Kond => ", A_norm, "\n")

print ("Inverse")
print (A_inv)
print ("Kond => ", A_inv_norm, "\n")


print ("Konditionszahl")
print (A_norm * A_inv_norm)
```
