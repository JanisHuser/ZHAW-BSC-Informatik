# Polynomial Regression


Künstliche Hypothese 
$$
h_{\theta}(z)
=
\theta_0 z_0 +
\theta_1 z_1 +
\theta_2 z_2 +
...
\theta_n z_n +
$$




```python
polynomial_features = PolynomialFeatures(degree=2)
x_poly = polynomial_features.fit_transform(X_train)
```

## Grad 2

Variable $a$ und $b$ haben folgende Optionen:
$$
1, a, a^2, b, b^2
$$

## Grad 3

Variable $a$ und $b$ haben folgende Optionen:
$$
1, a, a^2,  a^3, ab, a^2b, ab^2, b, b^2, b^3,  
$$

