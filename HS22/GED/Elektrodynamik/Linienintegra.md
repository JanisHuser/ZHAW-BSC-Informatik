
# Arbeitsintegrale

Ziehen wir ein Objekt mit einer konstanten Kraft $ \overrightarrow{F} $ über eine kurze Wegstrecke $ d \overrightarrow{r} $, leisten wir die Arbeit.

$$
dW = \overrightarrow{F}
\cdot
d \overrightarrow{r}
$$


$$
W = \int_{\gamma} \overrightarrow{F} \cdot d \overrightarrow{\gamma}
$$

## Pfad $ \gamma $
Pfad $ \gamma $ als Kurve im Raum mit Parameter s
$$
\overrightarrow{r}(s) = \overrightarrow{\gamma}(s) = 
\begin{pmatrix}
\gamma_x (s)\\
\gamma_y (s)\\
\gamma_z (s)
\end{pmatrix}



$$



**dW > 0***: Das Systen leistet Arbeit am Objekt

**dW < 0**: Das System bezieht Arbeit vom Objekt

# Linienintegral

Die Summe vieler kleiner Arbeitsintegrale gibt einenen Linienintegral

$$

W =
\int_{\gamma} \overrightarrow{F} \cdot d \overrightarrow{r}

\approx

\sum_{i=1}^4 \overrightarrow{F}(r_j) \cdot (\overrightarrow{r}_{i+1} - \overrightarrow{r}_i)

$$

## Spezialfall - Kreis

![Kreis](2F62570C-6FD0-4D56-99E3-C455A1AF3B19.jpeg)

$$
\int_{\gamma} \overrightarrow{U} \cdot d \overrightarrow{\gamma}
=
2 \pi r |\overrightarrow{U}|
$$


### Mit Vektoren
```python,editable
import numpy as np
radius = 1

# X, Y, Z Vector
U = np.array([1,2,3])

kraft = 2 * pi * np.absolute(U) 
print (kraft)

```

### Mit Vektorlänge
```python,editable
import numpy as np
radius = 1

# Absolute länge des Vektors
U = 3

kraft = 2 * pi * U
print (kraft)

```

## Spezialfall - Rechteckige Schlaufe

![Rechteckige Schleife](20EC7134-D1A8-425F-8AFF-0C68CB43F9A3.jpeg)

$$

\int_{\lambda} 
\overrightarrow{U}
\cdot
d
\overrightarrow{\lambda}

=
a
U_1
-
aU_5
$$

### Mit Vektoren
```python,editable
import numpy as np
u1 = np.array([1,2,3])
u5 = np.array([5,2,3])

a = 1

result = a* np.absolute(u1)- a*np.absolute(u5)

print (result)
```


### Mit Vektorlängen
```python,editable
import numpy as np
u1 = 5
u5 = 1

a = 1

result = a* u1- a*u5

print (result)
```