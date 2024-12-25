import os
def create_file():
    """Create the file if it does not exist."""
    if not os.path.exists("employees.txt"):
        with open("employees.txt", "w") as file:
            pass

def add_employee():
    """Add a new employee record."""
    with open("employees.txt", "a") as file:
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = input("Enter Salary: ")
        file.write(f"{emp_id}, {name}, {position}, {salary}\n")
        print("Employee record added successfully!")

def view_employees():
    """Display all employee records."""
    with open("employees.txt", "r") as file:
        records = file.readlines()
        if records:
            print("\nEmployee Records:")
            for record in records:
                print(record.strip())
        else:
            print("\nNo records found.")

def search_employee():
    """Search for an employee by Employee ID."""
    emp_id = input("Enter Employee ID to search: ")
    found = False
    with open("employees.txt", "r") as file:
        for record in file:
            if record.startswith(emp_id + ","):
                print("\nEmployee Details:")
                print(record.strip())
                found = True
                break
    if not found:
        print("Employee not found.")

def update_employee():
    """Update an employee's information."""
    emp_id = input("Enter Employee ID to update: ")
    updated_records = []
    found = False
    with open("employees.txt", "r") as file:
        records = file.readlines()
        for record in records:
            if record.startswith(emp_id + ","):
                found = True
                print("Enter new details (leave blank to keep current):")
                details = record.strip().split(", ")
                name = input(f"Name [{details[1]}]: ") or details[1]
                position = input(f"Position [{details[2]}]: ") or details[2]
                salary = input(f"Salary [{details[3]}]: ") or details[3]
                updated_records.append(f"{emp_id}, {name}, {position}, {salary}\n")
            else:
                updated_records.append(record)
    if found:
        with open("employees.txt", "w") as file:
            file.writelines(updated_records)
        print("Employee information updated successfully!")
    else:
        print("Employee not found.")

def delete_employee():
    """Delete an employee's record."""
    emp_id = input("Enter Employee ID to delete: ")
    updated_records = []
    found = False
    with open("employees.txt", "r") as file:
        records = file.readlines()
        for record in records:
            if record.startswith(emp_id + ","):
                found = True
                continue
            updated_records.append(record)
    if found:
        with open("employees.txt", "w") as file:
            file.writelines(updated_records)
        print("Employee record deleted successfully!")
    else:
        print("Employee not found.")

def main():
    create_file()
    while True:
        print("\nEmployee Records Manager")
        print("1. Add new employee record")
        print("2. View all employee records")
        print("3. Search for an employee by Employee ID")
        print("4. Update an employee's information")
        print("5. Delete an employee record")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()