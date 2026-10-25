** Is the dataset available? **
Number of Students contains at the data?
Number of classes?
Percent of failed students
# Example of required historical dataset. ##
 - Student ID
 - Program
 - Semester
 - Courses
 - Course Grades
 - GPA
 - Withdrawals
 - Repeated Courses
 - Credits Attempted
 - Credits Completed
 - Attendance
 - Early Assessments
   
# EDA
 * Missing Values
 * Duplicates
 * Outliers
 * Class Distribution
# calculate the Base Rate:
 * 12% of students are at risk
------ 
# Data Feasibility

## Dataset Availability
The dataset is available and contains synthetic academic student records.

- Number of Students: **100**
- Number of Student-Term Records: **212**
- Number of Academic Terms: **3**
- Academic Terms: **2025-Fall, 2026-Spring, 2026-Fall**

## Available Data
The dataset includes:
- Student ID
- Program
- Academic Term
- Courses and Course Outcomes
- Semester GPA
- Cumulative GPA
- Withdrawals
- Repeated Courses
- Credits Attempted
- Credits Completed
- Attendance
- Early Assessment Results
- Progression Status

## EDA

### Missing Values
- Attendance: **51.9%**
- Early Assessment Results: **61.3%**
- All other variables: **0%**

### Duplicates
- No duplicate records were found.

### Outliers
- No outliers were detected in Semester GPA or Cumulative GPA using the IQR method.

### Class Distribution
- Good Standing: **182**
- Academic Warning: **24**
- Probation: **6**

## Base Rate
Academic Warning and Probation were considered **At Risk**.

- At Risk: **30 records**
- Not At Risk: **182 records**
- Base Rate: **14.15%**

## Data Feasibility Conclusion
The dataset is suitable for the project. It contains multiple academic terms, relevant academic variables, and a measurable academic-risk outcome.

Missing values in Attendance and Early Assessment Results will need to be handled before modeling. Features will also need to be selected based on their availability at prediction time to avoid data leakage.