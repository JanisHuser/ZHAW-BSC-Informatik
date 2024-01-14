# Polynomial Regression

Assume the equation $h_{\theta} (x) = \theta_0 + \theta_1 x + \theta_2 x^2+ \theta_3 x^3$

1. Define artificial variables $z_0 = 1, z_1 = x, z_2 = z_3 = x^3, ...$
2. Reformulate the hypothesis as $h_{\theta} (x) = \theta_0 z_0+ \theta_1 z_1 + \theta_2 z_2+ \theta_3 z_3$
3. Apply gradient descent

## Over- and Underfitting

- Degree 1: Underfitting (too generic, does not predict well with new data)
- Degree 15: Overfitting (too precise on the data, does not predict well with new data)

![](https://github.zhaw.ch/pages/doem/mldm_book/pics/regression2/over-and-underfitting.png)

## Regularization

- The smaller the absolute values of the parameters $\theta$, the less extreme the curve will be.
- Regularization term depends **only** on the parameters $\theta$, not on the training samples.
- The hyperparamter $\lambda$ determines "how much" regularization counts:
	- The larger $\lambda$, the more the values of $\theta$ contribute to the cost
	



$$
J(\theta) = \frac{1}{2M}[
	\sum_{m=1}^{M} (y^{(m)} - h_{\theta} (x^{(m)}))^2 + 
	\lambda \sum_{j=1}^{n} \theta_j^2 
]
$$

- Large $\lambda$ will encourage the values of $\theta$ to stay rather small, and the prediction curve will be rather smooth.
- $\lambda$ close to zero means that values in $\theta$ might become very large, and hence the courve might jump around a lot.

## Hyperparameter tuning

1. Fit different values for $\lambda$
2. Evaluate the quality of the model using $R^2$ to determine which $\lambda$ works best.

We can use the following parameters when applying a polynomial regression
- degree of the polynomial
- learning rate


### Grid Search

The grid search algorithm finds the best parameter for many combinations. For each combination the MSE is calculated.