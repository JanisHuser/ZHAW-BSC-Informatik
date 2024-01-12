# Gradient Descent

The idea of gradient descent, is to find an optimal value for a problem. This is done using the **learning rate** $\alpha$. $\alpha$ is stepped towards the minimum, after every step the learning rate is decreased.

![](https://github.zhaw.ch/pages/doem/mldm_book/pics/regression2/gradient-descent-3d.png)

## Learning rate adjustments

![Learning rate adjustments](media/image-4.png)

## Generic Algorithm

1. Initialize $\theta_0, ... \theta_n$
2. Repeat until convergence
$$
\text{Update} \theta_j = \theta_j - \alpha \frac{\partial}{\partial \theta_j} J(\theta)   \qquad   \forall{j = 0, ..., n}
$$


## Learning Rate adjustments

$$
\alpha_t = \frac{1}{1 + \text{decay rate} * t} \alpha_0
$$