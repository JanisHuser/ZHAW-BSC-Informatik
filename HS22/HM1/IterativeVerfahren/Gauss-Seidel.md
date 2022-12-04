# Gauss-Seidel Verfahren
$$
x^{(k+1)}=D^{-1} (b - Lx^{(k+1)} - Rx^{(k)})
$$

## Algemeine Form

$$
x_{j}^{(k+1)}
=
\frac{1}{a_{ii}}
\left(
b_i - \sum_{j=1}^{i-1}a_{ij}x_j^{(k+1)}
-
\sum_{j=i+1}^n
a_{ij}x_j^{(k)}
\right)
$$
## Fixpunktiteration


$$
(D+L)x^{(k+1)}
=
-Rx^{(k)}
+b
$$
$$
x^{(k+1)}
=
-(D+L)^{-1}Rx^{(k)}
+ (D+L)^{-1}b
$$
