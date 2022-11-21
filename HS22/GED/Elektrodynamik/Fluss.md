# Fluss

## Ebene

```python
import numpy as np

# Fläche
A = 1

# Vektor
U = 2

print(A*U)
```

## Zylinder

### Feld senkrecth auf Mantel und parallel zu Boden
```python
import numpy as np

# Radius
r = 1

# Höhe 
h = 2
#Vektor
U = 2

print(2*np.pi*r*h*U)
```


### Feld senkrecth zu Boden
```python
import numpy as np

# Radius
r = 1

#Vektor
U = 2

print(2*np.pi*np.power(r,2)*U)
```


## Kugel
```python
import numpy as np

# Radius
r = 1

#Vektor
U = 2

print(4*np.pi*np.power(r,2)*U)
```
