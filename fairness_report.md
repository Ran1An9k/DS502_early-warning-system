# Fairness Report

## Purpose

This evaluation examines whether the selected Logistic Regression model shows noticeable performance differences across academic programs.

## Evaluation

The held-out test set contained 32 student-term records. Model performance was reviewed separately for each academic program using Precision and Recall.

| Program | Students | At Risk | Predicted At Risk | Precision | Recall |
|---|---:|---:|---:|---:|---:|
| Business Administration | 10 | 1 | 2 | 0.00 | 0.00 |
| Nursing | 3 | 0 | 1 | 0.00 | 0.00 |
| Psychology | 3 | 0 | 1 | 0.00 | 0.00 |
| Mechanical Engineering | 12 | 3 | 5 | 0.20 | 0.33 |
| Computer Science | 4 | 0 | 1 | 0.00 | 0.00 |

## Findings

The model detected one of the three at-risk cases in Mechanical Engineering, resulting in a recall of 0.33.

The single at-risk case in Business Administration was not detected.

Nursing, Psychology, and Computer Science contained no actual at-risk cases in the test set, so their recall values cannot be meaningfully interpreted.

False-positive predictions were observed across several programs.

## Limitation

The fairness results are exploratory because the test set is small and contains only four at-risk cases overall. Some programs contain no positive cases.

Therefore, these results are not sufficient to establish whether the model is fair or biased across academic programs.

A larger and more representative real-world dataset would be required for a reliable fairness assessment.