# Selektion

$$
\sigma_{query}
$$

1. Headers definieren (Liste von Liste)
2. Daten definieren (Liste von Liste)
3. Query (in Python Logik (and, or, >=, <=, \=\=, not, ...) definieren
4. Anwenden

```python
from Scripts.Select import Select

headers = [
    'A', 'B', 'C'
]

data = [
    [1, 0, 0],
    [1, 0, 1],
    [1, 1, 0],
    [0, 1, 0]
]

query = "((A == 0) or C == 2 * B)"

select = Select(headers, query)
new_data = select.do(data, True)

# NameError bedeuted, dass die Spalte fehlt

```

# Projektion

$$
\pi_{spalten}
$$

```python
from Scripts.Projection import Projection

headers = [
    'A', 'B', 'C'
]

data = [
    [1, 0, 0],
    [1, 0, 1],
    [1, 1, 0],
    [0, 1, 0]
]

columns = ['A', 'C']
# Setze erweiterungen, kann auch leer gelassen werden
extensions = [('2*A+C', 'X')]

projection = Projection(headers, columns, extensions)
new_data = projection.do(data, True)
```

# Umbenennung

$$
\rho_{\text{neuerName}}(R)
$$
