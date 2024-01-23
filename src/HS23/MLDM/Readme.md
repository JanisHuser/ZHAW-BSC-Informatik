# MLDM


# Confusion Matrix

[Confusion Matrix Calculator](https://confusionmatrixonline.com)

Types
- **TP**: True Positive, predicted==1 && actual==1
- **TN**: True Negative, predicted==0 && actual==0
- **FP**: False Positive, predicted==1 && actual==0
- **FN**: False Negative, predicted==0 && actual==1

Calculations
## Accuracy

$$
\frac{\text{TP}+\text{TN}}{\text{TP}+\text{TN}+\text{FP}+\text{FN}}
$$

## Precision

$$\frac{\text{TP}}{\text{TP}+\text{FP}}$$

## Recall/Sensitivity, True positive rate


Recall, also known as sensitivity or true positive rate, is a metric used to measure the performance of a classification model. Recall for a class in a binary classification task is calculated using the confusion matrix, which includes True Positives (TP), False Positives (FP), True Negatives (TN), and False Negatives (FN).

$$
\frac{\text{TP}}{\text{TP}+\text{FN}}
$$



## F1 Score

The F1 score is a metric used to measure a test's accuracy and considers both the precision and the recall of the test. It is particularly useful when the class distribution is imbalanced. The F1 score is the harmonic mean of precision and recall, providing a balance between them. It reaches its best value at 1 (perfect precision and recall) and worst at 0.


| | Actual Positives | Actual Negatives |
|-|------------------|------------------|
| Predicted Positives | TP | FP |
| Predicted Negative | FN | TN |



$$
2*
\frac{
    \text{precision} * \text{recall}
}
{
    \text{precision} + \text{recall}
}
$$


