# Trees

## Decision Trees

![](images/Decision%20Trees/IMG_0294.jpeg)

- Each node is labeled True (=left), and False (=right)
- Combines numeric and boolean decisions
- Numeric decisions can be repeated with different thresholds
- Leaf nodes can be repeated (e.g. "No Worries")

### Gini Impurity 


**The lower the better**

![](images/Decision%20Trees/IMG_0295.jpeg)

$$
1 -
\text{(Probability of yes)}^2
- 
\text{(Probability of No)}^2
$$


**Popcorn -> true** : $1 - (\frac{1}{1+3})^2 - (\frac{3}{1+3}) = 0.375$

**Popcorn -> false** : $1 - (\frac{2}{2+1})^2 - (\frac{2}{2+1}) = 0.444$

#### Gini Impurity for a Decision "Age < 9.5"

Weighted average of Gini Impurities of the leaves

**Popcorn:** $(\frac{4}{4+3}) * 0.375 + (\frac{3}{4+3}) * 0.444 = 0.402$

**Soda:** $0.214$

### Encoding

**Ordinal**: Assign integer values based on order of hierarchy

**Label**: Every category is converted into an integer value (e.g. by order of occurence - no mathematical interpretation)

**One-Hot**:For every category of a categorical variable a new binary variable is creatd: 1 represents the presence of that category and 0 represents the absence.

## Regression Trees

The process of building a regression tree involves recursively splitting the data into smaller subsets. At each step, the algorithm selects the feature and threshold that best splits the data. The goal is to split the data in such a way that the variance of the target variable is minimized within each subset.


You would use a Classification and Regression Tree (CART) when you need to perform either classification or regression tasks. 

1. Classification Tree: You would use a CART for classification when you want to **categorize data into different classes or groups** based on a set of features. For example, you could use a CART to predict whether an email is spam or not based on various email characteristics.

2. Regression Tree: You would use a CART for regression when you need to **predict a continuous** numerical value as the output. For instance, you could use a CART to predict the price of a house based on features like square footage, number of bedrooms, and location.

CART is a versatile algorithm that can be applied to a wide range of problems in machine learning and data analysis.


## Regularisation and Pruning


**Decision trees tend to overfit**


## Overfitting

![](images/Decision%20Trees/IMG_0296.jpeg)

### Pre Pruning

**Min-Sample Pruning**: Only split nodes with at least k samples

**Max-Depth Pruning** Restrict the maximum depths of a tree

### Post Pruning

Use Validation data to decide for each leaf wheter it is "reoonable"