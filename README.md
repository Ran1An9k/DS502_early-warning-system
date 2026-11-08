# Academic Early-Warning and Intervention System

## Overview

This project develops an academic early-warning system to identify students who may require academic support.

The system follows the workflow:

**Predict → Explain → Review → Intervene → Follow-up → Evaluate**

The project uses synthetic academic data to demonstrate the methodology and workflow.

## Dataset

The synthetic dataset contains:

- 100 unique students
- 212 student-term records
- 3 academic terms
- 5 academic programs

The target variable is `academic_risk`:

- 0 = Not At Risk
- 1 = At Risk

Academic Warning and Probation are classified as At Risk.

## Project Workflow

1. Data Feasibility
2. Feature Dictionary
3. Data Preparation and Pipeline
4. Logistic Regression Baseline
5. Decision Tree Candidate Model
6. Model Comparison and Selection
7. Fairness Evaluation
8. Explainability
9. Intervention Workflow
10. Monitoring and Drift
11. Final Documentation

## Models

Two models were evaluated:

- Logistic Regression
- Decision Tree

Logistic Regression was selected as the final model based on the overall evaluation, including PR-AUC, ROC-AUC, and probability calibration.

## Final Model Performance

Selected model: **Logistic Regression**

- Accuracy: 0.625
- Precision: 0.100
- Recall: 0.250
- F1 Score: 0.143
- ROC-AUC: 0.643
- PR-AUC: 0.387
- Selected Threshold: 0.23

## Main Project Files

- `data-feasibility.md`
- `feature-dictionary.md`
- `model-card.md`
- `fairness_report.md`
- `intervention-workflow.md`
- `monitoring-drift.md`
- `Model_Baseline_Complete.ipynb`
- `Decision_Tree_Complete.ipynb`
- `notebooks/Model_Comparison.ipynb`

## Important Note

This project uses synthetic data. The reported model performance demonstrates the project methodology and should not be interpreted as evidence of predictive validity on real students.

Model predictions are intended to support academic advisors and should not be used for automatic academic penalties or high-impact decisions.