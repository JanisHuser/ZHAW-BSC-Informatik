# Quadraturformel

$$
l_n (f: [a, b]) 
=
\sum_{i=0}^n
w_i f(x_i)
$$

**Exaktheitsgrad** $m$

**Ordnung** $m+1$

## Regeln

**Mittelpunktsregel**: $(b-a)f(\frac{a+b}{2})$

**Trapezregel**: $\frac{b-a}{2} (f(a) + f(b))$

**Simpsonregel**: $\frac{b-a}{6}(f(a) + 4f(\frac{a+b}{2})+f(b))$

## Summenregel

Der Intervall wird in $N$ gleich grosse Teile $[a_{k-1}, a_k]$ aufgeteilt.

$$
a_k = a + k \cdot \frac{b-a}{N}
$$

$$
y_k = \frac{a_k-1 + a_k}{2}
$$

**summierte Mittelpunktsregel**: $\frac{b-a}{N}(f(y_1) + f(y_2) + ... + f(y_N))$

**summierte Trapezregel**: $\frac{b - a}{2N} (f(a) + 2f(a_1) + 2f(a_2) + ... + 2f(a_{N-1}) + f(b))$

**summierte Simpsonregel**: $\frac{b-a}{6N}(f(a) + 4f(y_1) + 2f(a_1) + 4f(y_2) + ... + 2f(a_{N-1}) + 4f(y_N) + f(b))$