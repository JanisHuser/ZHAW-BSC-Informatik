## Zwei Funktionen auf Gleichheit prüfen
```python
import sympy as sp

from sympy.abc import x

a1 = sp.exp(x) - (sp.sqrt(2) +2)
a2 = sp.ln(sp.sqrt(x) + 2)


print ("Gleiche Funktion", a1.equals(a1))
```

