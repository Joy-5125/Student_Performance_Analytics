# Student Performance Analytics System

A beginner-friendly Python data-analysis mini project for the **Python with AI** assignment. It uses Python, NumPy, and Pandas to analyze student marks and attendance. It does **not** require machine learning.

## Features

- Loads student records from `students.csv` into a Pandas DataFrame.
- Calculates total marks and average marks for each student.
- Assigns grades using a defined grading scale.
- Marks a student Pass only if they score at least 40 in **each** subject.
- Reports highest, lowest, mean, and median student averages.
- Calculates pass/fail counts and pass percentage.
- Produces subject-wise and department-wise summaries.
- Lists the top five performers.
- Saves calculated results to CSV files.

## Files

- `main.py` — main program and reusable functions.
- `students.csv` — sample dataset containing 20 student records.
- `Project_Documentation.md` — project report/documentation.
- `Student_Performance_Analytics.ipynb` — Google Colab notebook version.
- `README.md` — project overview and run instructions.

## Dataset columns

| Column | Description |
|---|---|
| `Student_ID` | Unique student identifier |
| `Name` | Student name |
| `Department` | Student department |
| `Python_Marks` | Marks in Python, out of 100 |
| `NumPy_Marks` | Marks in NumPy, out of 100 |
| `Pandas_Marks` | Marks in Pandas, out of 100 |
| `Attendance` | Attendance percentage |

The included names and marks are sample data for demonstration.

## Grading and result rules

| Average marks | Grade |
|---:|:---|
| 90–100 | A+ |
| 80–89.99 | A |
| 70–79.99 | B |
| 60–69.99 | C |
| 50–59.99 | D |
| Below 50 | F |

**Pass rule:** a student must score at least 40 marks in every subject. Attendance is reported separately; attendance below 75% is labelled `Low` and does not change the marks-based Pass/Fail result in this sample implementation. Follow your trainer's rule if a different attendance condition is specified.

## Run in Google Colab

1. Open [Google Colab](https://colab.research.google.com/).
2. Upload `Student_Performance_Analytics.ipynb`, or create a new notebook.
3. Upload `students.csv` to the Colab session using the Files panel.
4. Run the notebook cells from top to bottom.
5. Check the printed analysis and the generated CSV output files.
6. Download the output files if required.

## Run locally

Install the dependencies:

```bash
pip install numpy pandas
```

Place `main.py` and `students.csv` in the same folder, then run:

```bash
python main.py
```

## Expected output

The program prints the dataset, each student's total/average/grade/result, class summary, subject-wise performance, department-wise performance, and top five students. It also creates `student_analysis_results.csv` and `subject_wise_summary.csv`.

## Assignment alignment

This project uses variables, data types, conditions, loops, functions, NumPy numerical calculations, Pandas DataFrames, filtering/grouping, and data analysis. It covers the requested totals, averages, grades, pass/fail, high/low/average performance, subject analysis, and top performers.
