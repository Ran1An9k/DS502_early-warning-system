# Model Card

## What Does This Model Predict?

The model predicts whether a student may require academic support.

The prediction is represented as:

- **0 = Not At Risk**
- **1 = At Risk**

The target variable was derived from academic progression status, where Academic Warning and Probation were classified as At Risk.

## Dataset

The model was developed using a synthetic academic dataset containing:

- 100 unique students
- 212 student-term records
- 3 academic terms
- 5 academic programs

Synthetic data was used to demonstrate the methodology and system workflow. Therefore, the reported performance does not establish predictive validity on real students.

## Purpose

To support early identification of students who may require academic support and prioritise academic advisor review.

## Users

- Academic Advisors

## Allowed Use

- Prioritising students for academic advisor review
- Supporting early academic intervention
- Assisting advisors in identifying students who may require additional support

## Prohibited Use

- Automatic suspension decisions
- Registration blocking
- Automatic academic penalties
- Student-facing risk scores
- Using model predictions without human review

## Model

**Selected Model:** Logistic Regression

Logistic Regression was selected as the final model after comparison with a Decision Tree model.

## Selected Threshold

**0.23**

The classification threshold was selected using the validation set.

## Test Performance

- Accuracy: **0.625**
- Precision: **0.100**
- Recall: **0.250**
- F1 Score: **0.143**
- ROC-AUC: **0.643**
- PR-AUC: **0.387**

The model detected 1 of the 4 at-risk cases in the held-out test set.

## Explainability

Logistic Regression coefficients and odds ratios can be used to examine how individual features contribute to model predictions.

Model predictions should support, rather than replace, academic advisor judgement.

## Fairness

Model performance was reviewed across academic programs.

The fairness analysis is exploratory because the test set is small and contains only four at-risk cases. Some academic programs contained no positive cases, so reliable conclusions about fairness or bias cannot be established.

## Limitations

- The project uses synthetic rather than real-world student data.
- The dataset and test set are small.
- The At Risk class is imbalanced.
- Only four At Risk cases were present in the test set.
- Model performance may not generalise to real students.
- Fairness results cannot be considered conclusive because of the limited sample size.
- The model identifies statistical patterns and does not establish causal relationships.

## Risks

- False negatives may result in at-risk students not being identified.
- False positives may result in unnecessary advisor reviews.
- Predictions may become less reliable if student data patterns change over time.
- The model should not be used for high-impact academic decisions without human review.