# Mittelpunktverfahren

## Mit Anzahl Iterationen
```python
def mittelpunktverfahren(f, a, b, n):
    h = (b - a) / n  # Berechne die Schrittweite
    result = 0.0
    
    for i in range(n):
        x = a + (i + 0.5) * h  # Berechne den Mittelpunkt des aktuellen Intervalls
        result += f(x)  # Addiere den Funktionswert am Mittelpunkt zum Ergebnis
    
    result *= h  # Multipliziere mit der Schrittweite, um das Integral zu approximieren
    return result


def f(x):
    return x**2

integral_approximation = mittelpunktverfahren(f, 0, 1, 100)
print(integral_approximation)
```

## Mit Schrittweite

```python
def mittelpunktverfahren(f, a, b, h):
    n = int((b - a) / h)  # Berechne die Anzahl der Teilintervalle
    result = 0.0
    
    for i in range(n):
        x = a + (i + 0.5) * h  # Berechne den Mittelpunkt des aktuellen Intervalls
        result += f(x)  # Addiere den Funktionswert am Mittelpunkt zum Ergebnis
    
    result *= h  # Multipliziere mit der Schrittweite, um das Integral zu approximieren
    return result

def f(x):
    return x**2

integral_approximation = mittelpunktverfahren(f, 0, 1, 0.1)
print(integral_approximation)
```