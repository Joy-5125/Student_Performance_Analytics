# Project Documentation: Student Performance Analytics System

## 1. Project Title
**Student Performance Analytics System**

Student Name: JOY GHOSH 
Course: Python with AI  

## 2. Objective
The objective is to build a Python-based system that reads student records and turns marks and attendance into understandable performance summaries. It helps identify students who are performing well, students who need support, the strongest subject, and differences between departments.

## 3. Technologies Used
- **Python:** variables, conditions, loops, functions, exception handling and program flow.
- **Pandas:** CSV loading, DataFrames, row-wise calculations, grouping and tabular output.
- **NumPy:** mean, median, maximum and minimum calculations.
- **CSV:** simple format for storing the dataset and exporting results.
- **Google Colab:** recommended environment for running the notebook.

No advanced machine-learning model is required or used.

## 4. Dataset Description
The supplied `students.csv` file contains 20 sample student records. The fields are:
- `Student_ID`: unique identifier.
- `Name`: student's name.
- `Department`: CSE, IT or ECE.
- `Python_Marks`, `NumPy_Marks`, `Pandas_Marks`: marks out of 100.
- `Attendance`: attendance percentage.

The data is illustrative sample data, not official student information.

## 5. Implementation
1. **Load data:** Pandas reads `students.csv` into a DataFrame.
2. **Validate data:** the program checks required columns, numeric values, missing values, and valid ranges for marks and attendance.
3. **Calculate total marks:** adds the three subject marks for each student.
4. **Calculate average marks:** calculates the mean of the three subject marks using Pandas and rounds it to two decimal places.
5. **Assign grades:** a reusable function maps the average to a grade.
6. **Determine result:** a student passes if all three subject marks are at least 40; otherwise, the result is Fail.
7. **Check attendance:** attendance of at least 75% is labelled Satisfactory; otherwise, it is labelled Low. This is a separate indicator and does not affect the marks-based result.
8. **Summarize class performance:** NumPy calculates the class mean, median, maximum and minimum average. Pandas calculates pass/fail counts and pass percentage.
9. **Analyze subjects:** a loop processes each subject to calculate its average, highest mark, lowest mark and number of students scoring at least 40.
10. **Analyze departments:** Pandas `groupby` summarizes student counts, average marks, passes and average attendance.
11. **Identify top performers:** students are sorted by average marks and the top five are displayed.
12. **Export results:** the program saves student results and subject summaries as CSV files.

## 6. Grading and Pass/Fail Rules
| Average marks | Grade |
|---:|:---|
| 90–100 | A+ |
| 80–89.99 | A |
| 70–79.99 | B |
| 60–69.99 | C |
| 50–59.99 | D |
| Below 50 | F |

A student passes only if the mark in **each** of Python, NumPy and Pandas is 40 or above. The 75% attendance threshold is reported separately. If the trainer provides a different rule, update the constants and logic accordingly.

## 7. Key Features
- CSV dataset with 20 records.
- Pandas DataFrame data handling.
- NumPy numerical calculations.
- Reusable functions for loading, grading, analysis and output.
- Loop-based subject analysis.
- Total and average marks for every student.
- Grade and pass/fail status.
- Highest, lowest, average and median performance.
- Subject-wise and department-wise summaries.
- Top five performers.
- Exported analysis CSV files.

## 8. Output
Run the notebook in Google Colab and capture screenshots of:
1. The dataset preview.
2. The student-wise results table.
3. The class performance summary.
4. The subject-wise and department-wise summaries.
5. The top five performers and saved output files.


## 9. Final Outcome
The project provides a readable summary of student performance from a CSV dataset. It calculates student totals and averages, assigns grades, identifies pass/fail status, compares subjects and departments, lists top performers, and exports the results for later review.

## 10. Challenges and Learning
Possible learning points include keeping CSV column names consistent, validating numeric data, choosing clear grading thresholds, using Pandas for tabular operations, using NumPy for numerical summaries, and separating calculations into reusable functions. Describe the actual issues you encountered after running and testing the project.


## 12. Testing Checklist
- [ ] `students.csv` contains at least 15–20 records.
- [ ] The notebook runs from top to bottom without errors.
- [ ] Totals and averages are displayed.
- [ ] Grades and pass/fail rules are applied.
- [ ] Subject-wise and department-wise analyses are displayed.
- [ ] Top performers are listed.
- [ ] CSV output files are generated.
