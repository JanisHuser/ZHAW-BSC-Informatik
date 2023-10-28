# SVM (Support Vector Machines)

Tries to find the "w" and "b" value in a way that maximizes the seperation between different classes of data points.



$$
b + w^T x = 0
$$

## Weight Vector (w)

- Tells how much each feature matters



## Bias Term (b)

- Is like an anchor point for the decision boundary. It shifts the boundary away from the origin


## Classification

The $y^{(m)}$ values in the context of Support Vector Machines (SVM) represent the decision function values for individual data points. These values can provide insights into how confidently and correctly the SVM classifies these data points. Here's how to interpret them:

1. **Positive Values of $y^{(m)}$:**
   - If $y^{(m)} > 0$, it means the SVM confidently classifies the data point as belonging to the class with a positive label. The larger the positive value, the higher the confidence in the classification.

2. **Negative Values of $y^{(m)}$:**
   - If \(y^{(m)} < 0\), it indicates the SVM confidently classifies the data point as belonging to the class with a negative label. The more negative the value, the higher the confidence in this classification.

3. **$y^{(m)}$ Near 0:**
   - If $y^{(m)}$ is close to 0, it suggests that the data point is located near the decision boundary. In this case, the SVM may be less certain about the classification.

4. **Magnitude of $y^{(m)}$:**
   - The magnitude of $y^{(m)}$ reflects the confidence level. Larger magnitude values indicate higher confidence in the classification, whether positive or negative.

So, you can use $y^{(m)}$ values to understand how well the SVM has classified individual data points. Large positive or negative values indicate strong confidence, values near 0 suggest proximity to the decision boundary, and the sign of the value indicates the predicted class.


## Calculate distance

```python
import numpy as np

# Assuming you have the weight vector 'w' from your trained SVM model
w = model.coef_[0]

# Calculate the margin width
margin_width = 2 / np.linalg.norm(w)

print("Margin Width:", margin_width)
```

## Scatterplot generieren

```python
import numpy as np
import matplotlib.pyplot as plt

# Assuming you have the feature data 'X' and class labels 'y'
# Also, the trained SVM model with optimized parameters: model, model.intercept_, model.coef_

# Scatterplot of data points
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired, s=30)

# Decision boundary
ax = plt.gca()
xlim = ax.get_xlim()
ylim = ax.get_ylim()

# Create a grid of points
xx, yy = np.meshgrid(np.linspace(xlim[0], xlim[1], 50),
                     np.linspace(ylim[0], ylim[1], 50))

# Calculate decision function values for the grid points
Z = model.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Plot decision boundary
plt.contour(xx, yy, Z, colors='k', levels=[-1, 0, 1], alpha=0.5, linestyles=['--', '-', '--'])

# Highlight the support vectors
plt.scatter(model.support_vectors_[:, 0], model.support_vectors_[:, 1],
            s=100, facecolors='none', edgecolors='k')

plt.title('SVM Decision Boundary with Gutters')
plt.show()
```


## Calculate accuraccy

```python
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC

# Create an SVM model with your preferred parameters
model = SVC(kernel='linear', C=1.0)

# Assuming you have feature data X and labels y

# Use cross_val_score to calculate accuracy
accuracy_scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')  # cv=5 for 5-fold cross-validation

# Calculate the mean accuracy
mean_accuracy = accuracy_scores.mean()

print("Mean Accuracy:", mean_accuracy)
```