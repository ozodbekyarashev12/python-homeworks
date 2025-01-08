import csv

# Step 1: Create the grades.csv file
grades_data = [
    {"Name": "Alice", "Subject": "Math", "Grade": 85},
    {"Name": "Bob", "Subject": "Science", "Grade": 78},
    {"Name": "Carol", "Subject": "Math", "Grade": 92},
    {"Name": "Dave", "Subject": "History", "Grade": 74},
]

grades_csv_path = "grades.csv"
average_grades_csv_path = "average_grades.csv"

# Writing initial grades data to the CSV
with open(grades_csv_path, mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["Name", "Subject", "Grade"])
    writer.writeheader()
    writer.writerows(grades_data)

# Step 2: Read data from grades.csv
subject_grades = {}
with open(grades_csv_path, mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        subject = row["Subject"]
        grade = int(row["Grade"])
        if subject not in subject_grades:
            subject_grades[subject] = []
        subject_grades[subject].append(grade)

# Step 3: Calculate average grades for each subject
average_grades = [
    {"Subject": subject, "Average Grade": sum(grades) / len(grades)}
    for subject, grades in subject_grades.items()
]

# Step 4: Write the average grades to average_grades.csv
with open(average_grades_csv_path, mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["Subject", "Average Grade"])
    writer.writeheader()
    writer.writerows(average_grades)

print(f"Files created: {grades_csv_path}, {average_grades_csv_path}")