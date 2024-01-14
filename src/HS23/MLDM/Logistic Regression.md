# Logistic Regression

Logistic regression classifies wether a value is "positive" or "negative. The value can be between 1.0 for positive and 0.0 for negative and represents how confident the machine is.

## Binary Classification

Classified into two sets, "positive" and "negative"

## K Fold

1. Split training set into K similar sized chunks
2. Fit model on K-1 sets, leave first one out
3. Predict model on left out set
4. Calc MSE
5. Repeate step 2-5 until 
4. Sum MSE from all above

Visual example on K=6 fold

| 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|
| P | F | F | F | F | F |
| F | P | F | F | F | F |
| F | F | P | F | F | F |
| F | F | F | P | F | F |
| F | F | F | F | P | F |
| F | F | F | F | F | P |




## Sigmoid functions

### Threshold

$$
h_{\theta}(x) = \begin{cases}
             1 & \text{if} \  \theta_0 + \theta_1 x > 0.5 \\
             0 & \text{if} \  \theta_0 + \theta_1 x \leq 0.5 \\
       \end{cases} \quad
$$

![](https://github.zhaw.ch/pages/doem/mldm_book/pics/logistic_regression/heartattack_step.png)

### Logistic Sigmoid

$$
g(z) = 

\frac{1}{1+e^{-z}}
$$

![](https://github.zhaw.ch/pages/doem/mldm_book/05_logistic_regression_files/figure-html/cell-2-output-1.png)

### Soft Step

$$
h_{\theta} (x)
= 
g(
	\theta_0 +
	\theta_1 x
)
$$

![](https://github.zhaw.ch/pages/doem/mldm_book/pics/logistic_regression/heartattack_sigmoid.png)


## Logistic Regression

$$
\^{y}
= h_{\theta}(x)
=
g(\theta_0 + \theta_1 x)

=
\frac{1}{1+e^{-(\theta_0+\theta_1x)}}
$$

### Multidimensional generalization

- $x$ is a vector of numbers
- $\theta^T x = \theta_0 x_0 + \theta_1 x_1 + ... + \theta_n x_n$

$$
\^y = h_{\theta}(x) = g(\theta^T x) = 
\frac{1}
{
	1 + e^{-\theta^T x}
}

$$

- $\theta$ detinermines the location and steepness of the soft step function
	- since $\theta$ influences the $g$ function, it is also dependent on the slope/steepness
	- the higher $\theta$, the higher the value of $g$ and therefore the steepness
- $\theta_0$ determines the bias (left and right shift along the x-axis)

### Training 

- Training must be done in an iterative approach.

### Cost Function
$$
\text{Loss}(h_0(x),y) =
\begin{cases}
             -log(h_{\theta}(x)) & \text{if} \ y=1 \\
             -log(1 - h_{\theta}(x)) & \text{if} \  y=0
       \end{cases} \quad
$$

can also be written as:

$$

\text{Loss}(h_{\theta}(x), y) = -y

log (h_{\theta}(x))
- 
(1 - y)
log (1 - h_{\theta}(x))
$$

$$
J(\theta) = \frac{1}{M}
\sum_{m=1}^{M}
\text{Loss}
(h_{\theta}(x^{(m)}), y^{(m)})
$$

## Multi class Classification

Classification often times requires to b