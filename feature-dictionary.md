# Feature Dictionary

This document describes the variables included in the academic early-warning dataset and their intended use in the project.

## Anonymous Student Identifier
- Description: Anonymous unique identifier for each student.
- Type: Categorical
- Available at prediction time: Yes
- Use in model: No

## Program
- Description: Student academic program.
- Type: Categorical
- Available at prediction time: Yes
- Use in model: Yes

## Academic Term
- Description: Academic term associated with the student record.
- Type: Categorical
- Available at prediction time: Yes
- Use in model: No

## Course Attempts
- Description: Number of courses attempted by the student during the academic term.
- Type: Numerical
- Available at prediction time: Yes
- Use in model: Yes

## Credits Attempted
- Description: Number of academic credits attempted by the student during the term.
- Type: Numerical
- Available at prediction time: Yes
- Use in model: Yes

## Credits Completed
- Description: Number of academic credits successfully completed by the student during the term.
- Type: Numerical
- Available at prediction time: No
- Use in model: No

## Course Outcomes
- Description: Final outcomes or grades for the courses taken during the term.
- Type: Text / Categorical
- Available at prediction time: No
- Use in model: No

## Semester GPA
- Description: GPA achieved by the student during the current academic term.
- Type: Numerical
- Available at prediction time: No
- Use in model: No

## Cumulative GPA
- Description: Student cumulative GPA up to the current academic term.
- Type: Numerical
- Available at prediction time: No
- Use in model: No

## Withdrawals
- Description: Number of courses withdrawn by the student during the academic term.
- Type: Numerical
- Available at prediction time: Yes, if the withdrawal occurred before the prediction point.
- Use in model: Yes, if available before the prediction point.

## Repeated Courses
- Description: Number of courses repeated by the student.
- Type: Numerical
- Available at prediction time: Yes, if based on previous academic history.
- Use in model: Yes

## Progression Status
- Description: Student academic standing during the academic term.
- Type: Categorical
- Available at prediction time: No
- Use in model: No, used to define the target variable.

## Attendance
- Description: Student attendance percentage during the academic term.
- Type: Numerical
- Available at prediction time: Yes, if measured by the prediction point.
- Use in model: Yes, if available by the prediction point.

## Early Assessment Results
- Description: Results from assessments completed early in the academic term.
- Type: Categorical
- Available at prediction time: Yes, if completed before the prediction point.
- Use in model: Yes, if available by the prediction point.



## Target Variable
The target variable is derived from Progression Status:

- Good Standing = Not At Risk (0)
- Academic Warning = At Risk (1)
- Probation = At Risk (1)