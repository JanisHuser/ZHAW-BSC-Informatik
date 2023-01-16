## Zwei Funktionen auf Gleichheit prüfen
```python
import sympy as sp

from sympy.abc import x

a1 = sp.exp(x) - (sp.sqrt(2) +2)
a2 = sp.ln(sp.sqrt(x) + 2)


print ("Gleiche Funktion", a1.equals(a1))
```

```python
import sympy as sp
from sympy.plotting import plot

f = "1/2 * 2 ** x"

# Create Sympy Equations
f = sp.sympify(f)
x = sp.symbols('x')
df = sp.diff(f, x) # Ableitung erstellen

x_limits = (1, 15)

plot(f, df,xlim=x_limits)
```
