"""
Student Performance Analytics System
Python + NumPy + Pandas mini project
Run in Google Colab or locally after installing numpy and pandas.
"""

import numpy as np
import pandas as pd

DATA_FILE = "students.csv"
SUBJECTS = ["Python_Marks", "NumPy_Marks", "Pandas_Marks"]
PASS_MARK = 40
MIN_ATTENDANCE = 75  # reported separately; passing is based on subject marks


def load_student_data(file_path=DATA_FILE):
    """Load the student CSV file into a Pandas DataFrame."""
    df = pd.read_csv(file_path)
    required_columns = [
        "Student_ID", "Name", "Department",
        "Python_Marks", "NumPy_Marks", "Pandas_Marks", "Attendance"
    ]
    missing = [column for column in required_columns if column not in df.columns]
    if missing:
        raise ValueError(f"Missing required column(s): {', '.join(missing)}")

    for column in SUBJECTS + ["Attendance"]:
        df[column] = pd.to_numeric(df[column], errors="raise")

    if df.empty:
        raise ValueError("The dataset contains no student records.")
    if df[SUBJECTS].isna().any().any() or df["Attendance"].isna().any():
        raise ValueError("Marks and attendance must not contain missing values.")
    if not df[SUBJECTS].apply(lambda col: col.between(0, 100).all()).all():
        raise ValueError("Subject marks must be between 0 and 100.")
    if not df["Attendance"].between(0, 100).all():
        raise ValueError("Attendance must be between 0 and 100.")
    return df


def assign_grade(average):
    """Assign a letter grade using the project's defined average-mark rules."""
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def calculate_student_results(df):
    """Calculate total, average, grade, pass/fail and attendance status."""
    result = df.copy()
    result["Total_Marks"] = result[SUBJECTS].sum(axis=1)
    result["Average_Marks"] = np.round(result[SUBJECTS].mean(axis=1), 2)
    result["Grade"] = result["Average_Marks"].apply(assign_grade)

    # A student passes only when they score at least 40 in every subject.
    result["Result"] = np.where(
        result[SUBJECTS].ge(PASS_MARK).all(axis=1), "Pass", "Fail"
    )
    result["Attendance_Status"] = np.where(
        result["Attendance"] >= MIN_ATTENDANCE, "Satisfactory", "Low"
    )
    return result


def show_dataset_summary(df):
    """Display basic information about the dataset."""
    print("\n" + "=" * 72)
    print("STUDENT DATASET")
    print("=" * 72)
    print(df.to_string(index=False))
    print(f"\nNumber of students: {len(df)}")
    print(f"Number of departments: {df['Department'].nunique()}")
    print("\nData types and non-null counts:")
    df.info()


def show_student_results(results):
    """Display student-wise calculated results."""
    columns = [
        "Student_ID", "Name", "Department", "Total_Marks",
        "Average_Marks", "Grade", "Result", "Attendance_Status"
    ]
    print("\n" + "=" * 72)
    print("STUDENT-WISE RESULTS")
    print("=" * 72)
    print(results[columns].sort_values("Average_Marks", ascending=False).to_string(index=False))


def show_class_summary(results):
    """Use NumPy and Pandas to calculate overall class statistics."""
    averages = results["Average_Marks"].to_numpy()
    print("\n" + "=" * 72)
    print("CLASS PERFORMANCE SUMMARY")
    print("=" * 72)
    print(f"Overall class average: {np.mean(averages):.2f}")
    print(f"Highest student average: {np.max(averages):.2f}")
    print(f"Lowest student average: {np.min(averages):.2f}")
    print(f"Median student average: {np.median(averages):.2f}")
    print(f"Students passed: {(results['Result'] == 'Pass').sum()}")
    print(f"Students failed: {(results['Result'] == 'Fail').sum()}")
    print(f"Pass percentage: {(results['Result'].eq('Pass').mean() * 100):.2f}%")
    print(f"Students with attendance >= {MIN_ATTENDANCE}%: "
          f"{results['Attendance_Status'].eq('Satisfactory').sum()}")


def show_subject_analysis(results):
    """Calculate subject-wise average, highest and lowest marks."""
    subject_rows = []
    for subject in SUBJECTS:  # loop through every subject
        marks = results[subject].to_numpy()
        subject_rows.append({
            "Subject": subject.replace("_Marks", ""),
            "Average_Marks": round(float(np.mean(marks)), 2),
            "Highest_Marks": int(np.max(marks)),
            "Lowest_Marks": int(np.min(marks)),
            "Students_Passed": int((marks >= PASS_MARK).sum())
        })
    subject_summary = pd.DataFrame(subject_rows).sort_values(
        "Average_Marks", ascending=False
    )
    print("\n" + "=" * 72)
    print("SUBJECT-WISE PERFORMANCE")
    print("=" * 72)
    print(subject_summary.to_string(index=False))
    best_subject = subject_summary.iloc[0]
    print(f"\nBest-performing subject by average: {best_subject['Subject']} "
          f"({best_subject['Average_Marks']:.2f})")
    return subject_summary


def show_department_analysis(results):
    """Compare average marks and pass counts by department."""
    summary = results.groupby("Department").agg(
        Students=("Student_ID", "count"),
        Average_Marks=("Average_Marks", "mean"),
        Passed=("Result", lambda values: (values == "Pass").sum()),
        Average_Attendance=("Attendance", "mean")
    ).round(2)
    print("\n" + "=" * 72)
    print("DEPARTMENT-WISE PERFORMANCE")
    print("=" * 72)
    print(summary.to_string())


def show_top_performers(results, top_n=5):
    """Show the top students ordered by average marks."""
    top_students = results.nlargest(top_n, "Average_Marks")[
        ["Student_ID", "Name", "Department", "Average_Marks", "Grade"]
    ]
    print("\n" + "=" * 72)
    print(f"TOP {min(top_n, len(results))} PERFORMING STUDENTS")
    print("=" * 72)
    print(top_students.to_string(index=False))


def save_results(results, subject_summary, output_file="student_analysis_results.csv"):
    """Save calculated student results to CSV for later use."""
    results.to_csv(output_file, index=False)
    subject_summary.to_csv("subject_wise_summary.csv", index=False)
    print(f"\nSaved student results to: {output_file}")
    print("Saved subject analysis to: subject_wise_summary.csv")


def main():
    """Run all project steps in sequence."""
    try:
        students_df = load_student_data()
        show_dataset_summary(students_df)
        results = calculate_student_results(students_df)
        show_student_results(results)
        show_class_summary(results)
        subject_summary = show_subject_analysis(results)
        show_department_analysis(results)
        show_top_performers(results, top_n=5)
        save_results(results, subject_summary)
        print("\nProject completed successfully.")
    except FileNotFoundError:
        print(f"Could not find '{DATA_FILE}'. Upload it to the Colab session "
              "or place it in the same folder as main.py.")
    except (ValueError, pd.errors.ParserError) as error:
        print(f"Please check the dataset: {error}")


if __name__ == "__main__":
    main()
