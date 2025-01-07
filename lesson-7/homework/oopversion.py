class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __repr__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"

    def to_string(self):
        return f"{self.employee_id},{self.name},{self.position},{self.salary}"

    @staticmethod
    def from_string(data_string):
        employee_id, name, position, salary = data_string.strip().split(",")
        return Employee(employee_id, name, position, float(salary))


class EmployeeManager:
    def __init__(self, file_name="employees.txt"):
        self.file_name = file_name

    def add_employee(self):
        employee_id = input("Enter Employee ID: ")
        if self.find_employee(employee_id):
            print("Error: Employee ID already exists.")
            return
        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = float(input("Enter Salary: "))
        new_employee = Employee(employee_id, name, position, salary)
        with open(self.file_name, "a") as file:
            file.write(new_employee.to_string() + "\n")
        print("Employee added successfully!")

    def view_employees(self):
        employees = self.get_all_employees()
        if not employees:
            print("No employee records found.")
        else:
            print("\nEmployee Records:")
            for employee in employees:
                print(employee)

    def search_employee(self):
        employee_id = input("Enter Employee ID to search: ")
        employee = self.find_employee(employee_id)
        if employee:
            print("\nEmployee Found:")
            print(employee)
        else:
            print("Error: Employee not found.")

    def update_employee(self):
        employee_id = input("Enter Employee ID to update: ")
        employees = self.get_all_employees()
        updated = False
        for i, employee in enumerate(employees):
            if employee.employee_id == employee_id:
                print(f"Current Details: {employee}")
                name = input("Enter New Name (or press Enter to keep current): ") or employee.name
                position = input("Enter New Position (or press Enter to keep current): ") or employee.position
                salary = input("Enter New Salary (or press Enter to keep current): ") or employee.salary
                employees[i] = Employee(employee_id, name, position, float(salary))
                updated = True
                break

        if updated:
            self.save_all_employees(employees)
            print("Employee updated successfully!")
        else:
            print("Error: Employee ID not found.")

    def delete_employee(self):
        employee_id = input("Enter Employee ID to delete: ")
        employees = self.get_all_employees()
        filtered_employees = [employee for employee in employees if employee.employee_id != employee_id]
        if len(filtered_employees) < len(employees):
            self.save_all_employees(filtered_employees)
            print("Employee deleted successfully!")
        else:
            print("Error: Employee ID not found.")

    def get_all_employees(self):
        employees = []
        try:
            with open(self.file_name, "r") as file:
                employees = [Employee.from_string(line) for line in file.readlines()]
        except FileNotFoundError:
            pass
        return employees

    def save_all_employees(self, employees):
        with open(self.file_name, "w") as file:
            for employee in employees:
                file.write(employee.to_string() + "\n")

    def find_employee(self, employee_id):
        employees = self.get_all_employees()
        for employee in employees:
            if employee.employee_id == employee_id:
                return employee
            return None
        def menu(self):
           while True:
            print("\nWelcome to the Employee Records Manager!")
            print("1. Add new employee record")
            print("2. View all employee records")
            print("3. Search for an employee by Employee ID")
            print("4. Update an employee's information")
            print("5. Delete an employee record")
            print("6. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_employee()
            elif choice == "2":
                self.view_employees()
            elif choice == "3":
                self.search_employee()
            elif choice == "4":
                self.update_employee()
            elif choice == "5":
                self.delete_employee()
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


# Run the program
if __name__ == "__main__":
    manager = EmployeeManager()
    manager.menu()