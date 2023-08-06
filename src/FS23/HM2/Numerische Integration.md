# Numerische Integration

Im Gegensatzu zur Ableitung, die für alle differenzierbaren Funktionen analytisch berechnet werden kann, können Integrale für eine Vielzahl von Funktionen nicht analytisch gelöst werden. Verfahren zur numerischen Integration (man spricht auch von Quadratur) spielen daher eine wichtige Rolle.

## Rechteckregel

```python
def rectangle_rule(f, a, b, n):
    """
    Approximates the integral of a function using the rectangle rule.

    Args:
    f: The function to integrate.
    a: The lower bound of the interval.
    b: The upper bound of the interval.
    n: The number of subdivisions (rectangles) for the approximation.

    Returns:
    The approximate value of the integral.
    """
    width = (b - a) / n
    integral = 0.0

    for i in range(n):
        x = a + i * width
        integral += f(x)

    integral *= width
    return integral

# Example usage
def f(x):
    return x**2  # Function to integrate

a = 0  # Lower bound
b = 1  # Upper bound
n = 100  # Number of subdivisions

approximation = rectangle_rule(f, a, b, n)
print("Approximated integral:", approximation)
```

### Summierte Rechteckregel

```python
import numpy as np

# Implementation
def sum_reckteck(f, a, b , h):
    n = int((b-a)/h)
    R = 0
    for i in range(0, n):
        x = a + i *h
        R = R + f(x+h/2)
    R = h*R
    
    return R

# Beispiel
def f(x):
    return 1./x

a = 2.
b = 4.
h = 0.5

R = sum_reckteck(f, a, b, h)
print ('R =', R)
```

## Trapezregel

```python
def trapezoidal_rule(f, a, b, n):
    """
    Approximates the integral of a function using the trapezoidal rule.

    Args:
    f: The function to integrate.
    a: The lower bound of the interval.
    b: The upper bound of the interval.
    n: The number of subdivisions (trapezoids) for the approximation.

    Returns:
    The approximate value of the integral.
    """
    width = (b - a) / n
    integral = 0.0

    for i in range(n):
        x0 = a + i * width
        x1 = a + (i + 1) * width
        integral += (f(x0) + f(x1)) / 2

    integral *= width
    return integral

# Example usage
def f(x):
    return x**2  # Function to integrate

a = 0  # Lower bound
b = 1  # Upper bound
n = 100  # Number of subdivisions

approximation = trapezoidal_rule(f, a, b, n)
print("Approximated integral:", approximation)
```

### Summierte Trapezregel

```python
import numpy as np

# Implementation
def sum_trapez(f, a, b , h):
    n = int((b-a)/h)
    T = (f(a) + f(b))/2
    for i in range(1, n):
        x = a + i *h
        T = T + f(x)
    T = h*T
    
    return T

# Beispiel
def f(x):
    return 1./x

a = 2.
b = 4.
h = 0.5

T = sum_trapez(f, a, b, h)
print ('T =', T)
```

## Simpson-Regel

```python
def simpson_rule(f, a, b, n):
    """
    Approximates the integral of a function using Simpson's rule.

    Args:
    f: The function to integrate.
    a: The lower bound of the interval.
    b: The upper bound of the interval.
    n: The number of subdivisions for the approximation (must be even).

    Returns:
    The approximate value of the integral.
    """
    h = (b - a) / n
    integral = 0.0

    for i in range(n):
        x0 = a + i * h
        x1 = x0 + h / 2
        x2 = x0 + h

        integral += (f(x0) + 4 * f(x1) + f(x2))

    integral *= h / 6
    return integral

# Beispielverwendung
def f(x):
    return x**2  # Funktion, die integriert werden soll

a = 0  # Untere Grenze
b = 1  # Obere Grenze
n = 100  # Anzahl der Unterteilungen (muss gerade sein)

approximation = simpson_rule(f, a, b, n)
print("Approximiertes Integral:", approximation)
```

### Summierte Sympsonregel
```python
def composite_simpson_rule(f, a, b, n):
    """
    Approximates the integral of a function using the composite Simpson's rule.

    Args:
    f: The function to integrate.
    a: The lower bound of the interval.
    b: The upper bound of the interval.
    n: The number of subdivisions for the approximation (must be even).

    Returns:
    The approximate value of the integral.
    """
    h = (b - a) / n
    x = [a + i * h for i in range(n + 1)]
    integral = 0.0

    for i in range(0, n, 2):
        integral += (f(x[i]) + 4 * f(x[i + 1]) + f(x[i + 2]))

    integral *= h / 3
    return integral

# Beispielverwendung
def f(x):
    return x**2  # Funktion, die integriert werden soll

a = 0  # Untere Grenze
b = 1  # Obere Grenze
n = 100  # Anzahl der Unterteilungen (muss gerade sein)

approximation = composite_simpson_rule(f, a, b, n)
print("Approximiertes Integral:", approximation)
```

### Fehler der Sympsonregel

```python

def composite_simpson_error(f, a, b, n):
    """
    Estimates the error of the composite Simpson's rule.

    Args:
    f: The function to integrate.
    a: The lower bound of the interval.
    b: The upper bound of the interval.
    n: The number of subdivisions for the approximation (must be even).

    Returns:
    The estimated error of the integral approximation.
    """
    h = (b - a) / n
    fourth_derivative = max(abs(fourth_derivative_func(f, x)) for x in numpy.linspace(a, b, 1000))
    error = -((b - a) * h**4 / 180) * fourth_derivative
    return error

def fourth_derivative_func(f, x):
    """
    Computes the fourth derivative of a function at a given point using finite differences.

    Args:
    f: The function.
    x: The point to evaluate the fourth derivative.

    Returns:
    The fourth derivative of the function at the given point.
    """
    h = 1e-5
    return (f(x - 2*h) - 4*f(x - h) + 6*f(x) - 4*f(x + h) + f(x + 2*h)) / h**4

```


## Romberg-Extrapolation

```python
def romberg_integration(f, a, b, n):
    """
    Approximates the integral of a function using Romberg integration.

    Args:
    f: The function to integrate.
    a: The lower bound of the interval.
    b: The upper bound of the interval.
    n: The number of iterations for the extrapolation.

    Returns:
    The approximate value of the integral.
    """
    r = [[0] * (n + 1) for _ in range(n + 1)]
    h = b - a

    r[0][0] = (f(a) + f(b)) * h / 2

    for i in range(1, n + 1):
        h /= 2
        sum_term = 0

        for j in range(1, 2**i, 2):
            sum_term += f(a + j * h)

        r[i][0] = r[i-1][0] / 2 + sum_term * h

        for k in range(1, i + 1):
            r[i][k] = r[i][k-1] + (r[i][k-1] - r[i-1][k-1]) / (4**k - 1)

    return r[n][n]

# Beispielverwendung
def f(x):
    return x**2  # Funktion, die integriert werden soll

a = 0  # Untere Grenze
b = 1  # Obere Grenze
n = 5  # Anzahl der Iterationen

approximation = romberg_integration(f, a, b, n)
print("Approximiertes Integral:", approximation)
```