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