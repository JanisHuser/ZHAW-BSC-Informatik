# Neural Networks

![](images/Neural%20Networks/IMG_0325.jpeg)

## Neuron

Applies an activation function to the weighted sum of its inputs plus a bias term.

![](images/Neural%20Networks/IMG_0323.jpeg)

## Deep Neural Networks

![](images/Neural%20Networks/IMG_0322.png)

Are Neural Networks with more than one hidden layer.

## Activation Functions

An activation function in neural networks introduces non-linearity to the model by determining the output of each neuron. Common activation functions include ReLU (Rectified Linear Unit) and Sigmoid, helping the network learn complex patterns and relationships in data during training.

![](images/Neural%20Networks/IMG_0324.jpeg)


## Softmax

Goal: For Classification tasks with mutually exclusive classese, in the output layer we want to have 1.0 for the correct class and 0 for all other classes.

![](images/Neural%20Networks/IMG_0326.jpeg)

## Training in Feedforward Neural Networks

![](images/Neural%20Networks/IMG_0327.jpeg)

[Ableitungsrechner](https://de.symbolab.com/solver/multivariable-partial-derivative-calculator/%5Cfrac%7B%5Cpartial%7D%7B%5Cpartial%20x%7D%5Cleft(y-%20x%5Cright)%5E%7B2%7D?or=input)

## Backpropagation

The **reuse of previous computations** (from later layers when computing the partial derivatives for earlier layers as those marked in blue) **makes backpropagation efficient**.

## Number of Parameters

- $n_i$: Number of neurons on layer $i$
- $n_{i-1}$: number of neurons on the previous layer
- $w_i$ number of weights connecting each neuron in layer $i-1$ to each neuron in layer $i$
- $b_i$ number of biases for each neuron in layer $i$

### Trainable Parameters per layer

$$
P_i = (n_{i-1} + 1) \times n_i
$$

### Total Trainable Parameters

$$

\sum\limits_{i=1}^{k} P_i
$$

### Number of Paths (HIDDEN LAYERS ONLY)

- $k$: Hidden layers
- $w$: Width

$$
w^{(k+1)}
$$

#### WITH ADDITIONAL INPUT LAYER

$$
$$
w^{(k+2)}
$$
$$