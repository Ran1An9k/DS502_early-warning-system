# Project Handover Memo

## Project
Academic Early-Warning and Intervention System

## Final Model
The final selected model is **Logistic Regression**.

The model was selected after comparison with a Decision Tree because it achieved better ROC-AUC, PR-AUC, and Brier Score, which are more informative for the imbalanced dataset.

Selected threshold: **0.23**

## Data
The project uses a **synthetic dataset** containing:

- 100 students
- 212 student-term records
- 3 academic terms
- 5 academic programs

The target variable is `academic_risk`:

- 0 = Not At Risk
- 1 = At Risk

At Risk includes students with Academic Warning or Probation.

## How to Run the Model

Run:

`Model_Baseline_Complete.ipynb`

Run all cells in order to reproduce the preprocessing, model training, threshold selection, evaluation, calibration, and saved results.

## Safe Retraining

When new data becomes available:

1. Use only information available at the defined prediction time.
2. Do not include leakage variables such as final GPA, final course outcomes, progression status, or credits completed.
3. Run the same preprocessing pipeline.
4. Retrain using historical data only.
5. Validate the model before replacing the current version.
6. Do not retrain automatically when drift is detected.

Students who received interventions should be identified before future retraining because their outcomes may have been affected by the intervention.

## Changing the Threshold

The current threshold is **0.23**.

If the threshold is changed:

1. Evaluate the new threshold using validation data.
2. Compare Precision, Recall, and F1.
3. Record the reason for the change.
4. Record the old and new threshold values.
5. Update the model documentation.

The test set should not be used to select the threshold.

## Re-running the Fairness Audit

Fairness should be evaluated across academic programs.

For each program, review:

- Precision
- Recall
- False positives
- False negatives

Because the current dataset and test set are small, fairness results should be considered exploratory and should not be used to make strong conclusions about bias.

## Monitoring

Future versions should monitor:

- Precision
- Recall
- F1
- PR-AUC
- Calibration
- False positive and false negative rates
- Distribution of predicted risk
- Changes in feature distributions across academic terms

If significant drift is detected, the model should be reviewed and validated before retraining.

## Important Limitations

This project uses synthetic data.

Therefore, the reported predictive performance demonstrates the methodology and implementation of the system but does not establish predictive validity on real students.

The system is intended only as an academic advisor decision-support tool and must not automatically make academic or disciplinary decisions.