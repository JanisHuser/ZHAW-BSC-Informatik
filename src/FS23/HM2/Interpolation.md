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

xp = 11

m = len(x)

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
# Define the original data points
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 5, 3]

# Define the points where you want to estimate values
x_new = [1.5, 3.5]

# Perform spline interpolation
y_new = []
for xi in x_new:
    # Find the interval where xi lies
    for i in range(len(x) - 1):
        if x[i] <= xi <= x[i + 1]:
            h = x[i + 1] - x[i]
            t = (xi - x[i]) / h

            # Calculate the estimated y-value using cubic spline interpolation formula
            a = (-t**3 + 2 * t**2 - t) * y[i]
            b = (3 * t**3 - 5 * t**2 + 2) * y[i + 1]
            c = (-3 * t**3 + 4 * t**2 + t) * (y[i + 1] - y[i]) / h
            d = (t**3 - t**2) * (y[i + 1] - y[i]) / h

            y_new.append(a + b + c + d)
            break

print(y_new)
```