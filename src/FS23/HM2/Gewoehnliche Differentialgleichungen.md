# Gewöhnliche Differentialgleichung
In vielen Prozessen in der Natur oder Technik spielen zeitliche Änderungen von beobachtbaren Grössen ('Observablen'), nennen wir z.B. $y(t)$ eine wichtige Rolle. Häufig ist die zeitliche Änderung einer solchen Grösse, also $\frac{d_y}{d_t}$, abhängig von der Grösse $y(t)$ selbst, d.h. wir können $\frac{d_y}{d_t}$ durch eine Funktion $f$ ausdrücken, die von der Zeit $t$ aber eben auch von der eigentlichen Grösse $y(t)$ abhängt:

$$
\frac{d_y}{d_t}
= f(t, y(t))
$$


## Richtungsfeld

```python
import numpy as np
import matplotlib.pyplot as plt

def dy_dx(x, y):
    return x + y

x = np.linspace(-5, 5, 20)  # x-Werte im Bereich von -5 bis 5
y = np.linspace(-5, 5, 20)  # y-Werte im Bereich von -5 bis 5

X, Y = np.meshgrid(x, y)
U = 1  # x-Komponente der Vektoren (konstant 1)
V = dy_dx(X, Y)  # y-Komponente der Vektoren basierend auf der Differentialgleichung

plt.quiver(X, Y, U, V)  # Richtungsfeld zeichnen
plt.xlabel('x')
plt.ylabel('y')
plt.title('Richtungsfeld der Differentialgleichung dy/dx = x + y')
plt.grid(True)
plt.show()
```

## Euler Verfahren
```python

import numpy as np
import matplotlib.pyplot as plt

def dy_dx(x, y):
    return x + y

def euler_method(f, x0, y0, h, num_steps):
    x = np.zeros(num_steps + 1)
    y = np.zeros(num_steps + 1)
    x[0] = x0
    y[0] = y0

    for i in range(num_steps):
        y[i+1] = y[i] + h * f(x[i], y[i])
        x[i+1] = x[i] + h

    return x, y

x = np.linspace(-5, 5, 20)  # x-Werte im Bereich von -5 bis 5
y = np.linspace(-5, 5, 20)  # y-Werte im Bereich von -5 bis 5

X, Y = np.meshgrid(x, y)
U = 1  # x-Komponente der Vektoren (konstant 1)
V = dy_dx(X, Y)  # y-Komponente der Vektoren basierend auf der Differentialgleichung

plt.quiver(X, Y, U, V)  # Richtungsfeld zeichnen

# Lösungskurve berechnen
x0 = 0  # Anfangswert für x
y0 = 3  # Anfangswert für y
h = 0.1  # Schrittweite
num_steps = 100  # Anzahl der Schritte

x_sol, y_sol = euler_method(dy_dx, x0, y0, h, num_steps)
plt.plot(x_sol, y_sol, 'r', label='Lösungskurve für y(0) = 3')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Richtungsfeld und Lösungskurve der Differentialgleichung dy/dx = x + y')
plt.grid(True)
plt.legend()
plt.show()
```

## Runge Kutta Verfahren

```python

def runge_kutta(f, x0, y0, h, num_steps):
    x = [x0]
    y = [y0]

    for i in range(num_steps):
        k1 = h * f(x[i], y[i])
        k2 = h * f(x[i] + h/2, y[i] + k1/2)
        k3 = h * f(x[i] + h/2, y[i] + k2/2)
        k4 = h * f(x[i] + h, y[i] + k3)

        x.append(x[i] + h)
        y.append(y[i] + (k1 + 2*k2 + 2*k3 + k4) / 6)

    return x, y

def dy_dx(x, y):
    return x + y

x0 = 0  # Anfangswert für x
y0 = 3  # Anfangswert für y
h = 0.1  # Schrittweite
num_steps = 100  # Anzahl der Schritte

x_sol, y_sol = runge_kutta(dy_dx, x0, y0, h, num_steps)

plt.plot(x_sol, y_sol, 'r', label='Lösungskurve für y(0) = 3')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Lösungskurve der Differentialgleichung dy/dx = x + y mit dem Runge-Kutta-Verfahren')
plt.grid(True)
plt.legend()
plt.show()
```


### Runge Kutta in Vektorieller Form

```python

import numpy as np
import matplotlib.pyplot as plt


def rk4_vektor(f, a, b, y0, h):
    x = np.arange(a, b + h, h)
    y = np.zeros((y0.size, x.size))
    n = x.size
    # AB
    y[:, 0] = y0

    for i in range(0, n-1):
        k1 = f(x[i], y[:, i])
        k2 = f(x[i] + h / 2, y[:, i] + h / 2 * k1)
        k3 = f(x[i] + h / 2, y[:, i] + h / 2 * k2)
        k4 = f(x[i] + h, y[:, i] + h * k3)
        y[:, i + 1] = y[:, i] + h/6 * (k1 + 2*k2 + 2*k3 + k4)

    return x, y


def fh(t, z):
    u = (300000.0 - 80000.0) / 190.0
    vrel = 2600.0
    ma = 300000.0
    g = 9.81
    z1 = z[0]
    z2 = z[1]
    return np.array([z2, vrel*(u/(ma - u * t)) - g - (np.exp(-z1/8000.0)/(ma - u * t)) * z2**2])


# Tstart
a = 0.

# Tende
b = 190.0

h = 0.1

# h(0) = h'(0) = 0
y0 = np.array([0.0, 0.0])

# z[0] = z1 = h(t); z[1] = z2 = v(t)
x, z = rk4_vektor(fh, a, b, y0, h)


def z3(t, z):
    u = (300000.0 - 80000.0) / 190.0
    vrel = 2600.0
    ma = 300000.0
    g = 9.81
    z1 = z[0]
    z2 = z[1]
    return vrel*(u/(ma - u * t)) - g - (np.exp(-z1/8000.0)/(ma - u * t)) * z2**2


plt.plot(x, z[0, :], label="h(t)")
plt.title("h(t)")
plt.grid()
plt.figure()
plt.plot(x, z[1, :], label="v(t)")
plt.title("v(t)")
plt.grid()
plt.figure()
plt.plot(x, z3(x, z), label="a(t)")
plt.title("a(t)")
plt.grid()

plt.show()

```


## Stabilitätsfunktion

```python
import numpy as np
import matplotlib.pyplot as plt

def stability_function(z):
    return 1 + z + 0.5*z**2 + (1/6)*z**3 + (1/24)*z**4

z = np.linspace(-5, 5, 100)  # Werte für z im Bereich von -5 bis 5
S = stability_function(z)

plt.plot(z, np.abs(S), label='|Stabilitätsfunktion|')
plt.xlabel('Re(z)')
plt.ylabel('|Stabilitätsfunktion|')
plt.title('Stabilitätsfunktion des Runge-Kutta-Verfahrens (RK4)')
plt.grid(True)
plt.legend()
plt.show()
```