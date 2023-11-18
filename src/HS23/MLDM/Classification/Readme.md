# Clasification

The training data comes in pairs. Yet the target values $y$ belong to a *finite* set. The goal is to pick the correct one as often as possible.

- Analyzing a text to determine if the sentiment is happy or sad.
- Using hockey players' statistics to predict which of two teams will probably win a match.
- Analyzing a song to determine if it is classical, techno, pop, or rock.

## Binary Classification

There are only two classes to distinguish, typically "positive" or "negative".

## Logistic Regression


$$
\^{y} = h_{\theta} (x) = g(\theta_0 + \theta_1 x) = 
\frac{
    1
}{
    1 + e^{-(\theta_0 + \theta_1 x)}
}
$$

### If x is a Vector

$$
\^{y} = h_{\theta}(x) = g(\theta^T x)
= 
\frac{1}
{
    1 + e^{-(\theta^{T} x)}
}
$$

### Training

#### Loss Function
$$
\text{Loss}(h_{\theta_0},y)
=
-y 
log(h_{\theta}(x)) - (1-y)log(1- h_{\theta}(x))
$$

#### Cost Function

$$
J(\theta)
=
\frac{1}{M}
\sum\limits_{m=1}^{M}
\text{Loss}(h_{\theta}(x_m), y_m)
$$

## Evaluation

- Comparing training and testing result. If training accuracy is nearly 100%, it is overfitting.
- Since testing data is new data, it is used to test the accuracy on completely new data


# Confusion Matrix

**T** = True
**F** = False

**Precision:** TPos / (TPos + TNeg + TNeu)

**Recall:** TPos / (TPos / FNeg / FNeu)

**F-Measure:** 2*precision * recall (precision + recall)

**Accuracy:** (all true) / (all data)
