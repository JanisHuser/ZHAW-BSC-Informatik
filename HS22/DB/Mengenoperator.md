
# Vereinigung

$$
R \cup S
$$
```python
from Scripts.Sets.Union import SetUnion

header = [
    'Name', 'Adresse', 'Geschlecht', 'Geburt'
]

data_r = [
    ['Carrie Fisher', '123 Mapple St.', 'F', '999']
]

data_s = [
    ['Carrie Fisher', '123 Mapple St.', 'F', '999'],
    ['New DATA HERE', '123 Mapple St.', 'F', '999']
]

union = SetUnion(header)

unified_data = union.do(data_r, data_s, True)
```

# Durchschnitt 

$$
R \cap b
$$

```python
from Scripts.Sets.Intersect import SetIntersect

header = [
    'Name', 'Adresse', 'Geschlecht', 'Geburt'
]

data_r = [
    ['Carrie Fisher', '123 Mapple St.', 'F', '999']
]

data_s = [
    ['Carrie Fisher', '123 Mapple St.', 'F', '999'],
    ['New DATA HERE', '123 Mapple St.', 'F', '999']
]

intersect = SetIntersect(header)

intersected_data = intersect.do(data_r, data_s, True)
```

# Differenz
$$
R \backslash S
$$
$$
R - S
$$

```python
from Scripts.Sets.Subtract import SetSubtract

header = [
    'Name', 'Adresse', 'Geschlecht', 'Geburt'
]

data_r = [
    ['Carrie Fisher', '123 Mapple St.', 'F', '999'],
    ['New DATA HERE', '123 Mapple St.', 'F', '999']
]

data_s = [
    ['Carrie Fisher', '123 Mapple St.', 'F', '999'],   
]

subtract = SetSubtract(header)
subtracted_data = subtract.do(data_r, data_s, True)
```

## Duplikate entfernen

$$
\phi
$$
```python
from Scripts.Sets.Set_Helpers import remove_duplicates
data_r = [
    ['Carrie Fisher', '123 Mapple St.', 'F', '999'],
    ['Carrie Fisher', '123 Mapple St.', 'F', '999'],
    ['New DATA HERE', '123 Mapple St.', 'F', '999']
]

setified = remove_duplicates(data_r)
for row in setified:
    print (*row, sep='\t')
```