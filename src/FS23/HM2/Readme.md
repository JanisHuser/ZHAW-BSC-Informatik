<p style="page-break-before: always"/>

# HM2


## Ableitung in Python
```python
from sympy import *
import numpy as np

x = Symbol('x')
y = x**2 + 1

yprime = y.diff(x)
print(yprime)
```