# Interpolation
Die Interpolation ist ein Speziialfall der linearen Ausgleichsrechnung, bei dem wir zu einer Menge von vorgegebenen Punkten eine Funktion suchen, die exakt (und nicht nur näherungsweise) durch diese Punkte verläuft.


## Polynominterpolation

```python
#Sample data points
x = [1, 2, 3, 4, 5]
y = [2, 1, 3, 2, 4]

#Polynomial interpolation
n = len(x)
coefficients = []

for k in range(n):
    numerator = 1
    denominator = 1

    for j in range(n):
        if j != k:
            numerator *= (x[k] - x[j])
            denominator *= (x[k] - x[j])

    coefficient = y[k] * (numerator / denominator)
    coefficients.append(coefficient)

#Evaluate the polynomial at a specific point
x_new = 2.5
y_new = sum(coefficients[i] * x_new**(n-1-i) for i in range(n))

print("Interpolated value at x =", x_new, "is y =", y_new)
```

## Lagrange Interpolation

```python
x = [8.00, 10.00, 12.00, 14.00]
y = [11.2, 13.4, 15.3, 19.5]

#X für welches y berechnet werden soll  
xp = 11

m = len(x)

#Grad des Polynoms
n = m -1
yp = 0

for i in range(n+1):
    p = 1
    for j in range(n+1):
        if j != i:
            p *= (xp - x[j])/(x[i] - x[j])
    yp += y[i] * p
    
print (f"Y Wert für x= {xp}: {yp}")
```



## Splineinterpolation

```python
# Function to calculate the cubic spline coefficients
def calculate_spline_coefficients(x, y):
    n = len(x)
    h = [x[i+1] - x[i] for i in range(n-1)]
    
    # Calculate the tridiagonal matrix coefficients
    alpha = [0] + [3 * (y[i+1]-y[i])/h[i] - 3 * (y[i]-y[i-1])/h[i-1] for i in range(1, n-1)] + [0]
    l = [1] + [0] * (n-2) + [0]
    mu = [0] * (n-1) + [1]
    z = [0] * n
    
    # Solve the tridiagonal matrix
    for i in range(1, n):
        l[i] = 2 * (x[i+1] - x[i-1]) - h[i-1] * mu[i-1]
        mu[i] = h[i] / l[i]
        z[i] = (alpha[i] - h[i-1] * z[i-1]) / l[i]
    
    # Calculate the spline coefficients
    c = [0] * n
    b = [0] * (n-1)
    d = [0] * (n-1)
    l[n-1] = 1
    z[n-1] = 0
    
    for j in range(n-2, -1, -1):
        c[j] = z[j] - mu[j] * c[j+1]
        b[j] = (y[j+1] - y[j])/h[j] - h[j] * (c[j+1] + 2 * c[j]) / 3
        d[j] = (c[j+1] - c[j]) / (3 * h[j])
    
    return y[:-1], b, c[:-1], d

# Function to perform spline interpolation
def spline_interpolation(x, y, new_x):
    coefficients = calculate_spline_coefficients(x, y)
    x_i, b, c, d = coefficients
    
    interpolated_y = []
    for i in range(len(new_x)):
        # Find the interval where new_x[i] falls
        for j in range(len(x_i)-1, -1, -1):
            if new_x[i] >= x_i[j]:
                break
        
        # Perform spline interpolation
        delta_x = new_x[i] - x_i[j]
        interpolated_value = y[j] + b[j]*delta_x + c[j]*(delta_x**2) + d[j]*(delta_x**3)
        interpolated_y.append(interpolated_value)
    
    return interpolated_y

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 1, 3, 4, 2]

# New x values for interpolation
new_x = [1.5, 2.5, 3.5, 4.5]

# Perform spline interpolation
new_y = spline_interpolation(x, y, new_x)

print(new_y)
```