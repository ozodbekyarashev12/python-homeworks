import csv
from collections import defaultdict

# Function to read grades from the CSV file and store them in a list of dictionaries
def read_grades(file_name):
    grades_data = []
    with open(file_name, mode='r', newline='') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            grades_data.append({
                'Name': row['Name'],
                'Subject': row['Subject'],
                'Grade': int(row['Grade'])
            })
    return grades_data

# Function to calculate the average grade for each subject
def calculate_average_grades(grades_data):
    subject_grades = defaultdict(list)
    # Group grades by subject
    for entry in grades_data:
        subject_grades[entry['Subject']].append(entry['Grade'])
    
    # Calculate the average for each subject
    average_grades = {}
    for subject, grades in subject_grades.items():
        average_grades[subject] = sum(grades) / len(grades)
    
    return average_grades

# Function to write the average grades to a new CSV file
def write_average_grades(file_name, average_grades):
    with open(file_name, mode='w', newline='') as file:
        fieldnames = ['Subject', 'Average Grade']
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        csv_writer.writeheader()
        
        for subject, avg_grade in average_grades.items():
            csv_writer.writerow({'Subject': subject, 'Average Grade': round(avg_grade, 2)})

# Main function
def main():
    # Read grades from the grades.csv file
    grades_data = read_grades('grades.csv')
    
    # Calculate average grades for each subject
    average_grades = calculate_average_grades(grades_data)
    
    # Write the average grades to the average_grades.csv file
    write_average_grades('average_grades.csv', average_grades)
    print("Average grades have been written to 'average_grades.csv'.")

if __name__ == "__main__":
    main()
