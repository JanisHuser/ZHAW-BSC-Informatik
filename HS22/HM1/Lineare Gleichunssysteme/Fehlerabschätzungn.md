
# A-Priori Geschätzte Iterationen
```python
def estimate_iteration(B, x0, x1, tol):

B_norm = np.linalg.norm(B, np.inf)

x_norm = np.linalg.norm(x1 - x0, np.inf)

n = np.log(((1 - B_norm) / x_norm) * tol) / np.log(B_norm)

return n
```

```python
import numpy as np
from Scripts.LinalgHelpers import calc_a_posteriori_error, calc_a_priori_iteration

calc_a_posteriori_error()
calc_a_priori_iteration()
```


## Bei Funktionen


```python
from Scripts.FuncHelper import calc_a_priori_iteration

f = "exp(x) - (sqrt(2) +2)"

tolerance = 10**(-7)
x0 = 0.5
a = 0.5    # Startwert der Range
print("Iterationen:", calc_a_priori_iteration(f, x0, a, tolerance))
```

