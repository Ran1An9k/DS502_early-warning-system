# Monitoring and Drift

## Purpose

The model should be monitored after deployment to ensure that its performance remains stable over time.

## Monitoring

The following should be monitored periodically:

- Prediction performance
- Precision
- Recall
- F1 Score
- PR-AUC
- False Positive and False Negative rates
- Distribution of At Risk predictions

## Data Drift

Data drift occurs when the characteristics of new student data change compared with the data used to train the model.

Examples include:

- Changes in attendance patterns
- Changes in early assessment results
- Changes in the distribution of academic programs
- Changes in the proportion of students identified as At Risk

## Performance Drift

Performance drift occurs when the model becomes less accurate over time.

The model should be reviewed if:

- Recall decreases noticeably
- PR-AUC decreases
- False Negative rates increase
- Prediction patterns change significantly between academic terms

## Model Review

If significant drift is detected:

1. Review the new data.
2. Re-evaluate model performance.
3. Check for changes in feature distributions.
4. Retrain the model using updated historical data if necessary.
5. Validate the updated model before deployment.

## Limitation

Because the current project uses synthetic data, the monitoring framework demonstrates the proposed methodology only. Real-world monitoring would require actual longitudinal student data.