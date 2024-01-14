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

Types
- **TP**: True Positive, predicted==1 && actual==1
- **TN**: True Negative, predicted==0 && actual==0
- **FP**: False Positive, predicted==1 && actual==0
- **FN**: False Negative, predicted==0 && actual==1

Calculations
- **Accuracy:** $\frac{\text{TP}+\text{TN}}{\text{TP}+\text{TN}+\text{FP}+\text{FN}}$
- **Precision**: $\frac{\text{TP}}{\text{TP}+\text{FP}}$
- **Recall/Sensitivity, True positive rate**: $\frac{\text{TP}}{\text{TP}+\text{FN}}$
- **F1 Score**: $\frac{2*\text{TP}}{2*\text{TP}+\text{FP}+\text{FN}}$


| | Actual Positives | Actual Negatives |
|-|------------------|------------------|
| Predicted Positives | TP | FP |
| Predicted Negative | FN | TN |