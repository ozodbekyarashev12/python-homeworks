import json
import csv


class Task:
    def __init__(self, task_id, title, description, due_date=None, status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def __repr__(self):
        return f"{self.task_id}, {self.title}, {self.description}, {self.due_date}, {self.status}"

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status,
        }

    @staticmethod
    def from_dict(data):
        return Task(
            data["task_id"],
            data["title"],
            data["description"],
            data.get("due_date"),
            data.get("status", "Pending"),
        )


class TaskManager:
    def __init__(self, file_name="tasks.json", file_format="json"):
        self.file_name = file_name
        self.file_format = file_format
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        try: 
            with open(self.file_name, "r") as file:
                tasks_data = json.load(file)
                self.tasks = [Task.from_dict(data) for data in tasks_data]
        except FileNotFoundError:
            print("no tasks file found, initializing with an empty task list")
        except json.JSONDEcodeError:
             print("Error: Could not parse the task file. Initializing with an empty task list.")
             self.task=[]
                   

    def add_task(self):
        task_id = input("Enter Task ID: ")
        if self.find_task(task_id):
            print("Error: Task ID already exists.")
            return
        title = input("Enter Title: ")
        description = input("Enter Description: ")
        due_date = input("Enter Due Date (YYYY-MM-DD or leave blank): ")
        status = input("Enter Status (Pending/In Progress/Completed): ") or "Pending"
        new_task = Task(task_id, title, description, due_date, status)
        self.tasks.append(new_task)
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("\nTasks:")
            for task in self.tasks:
                print(task)

    def update_task(self):
        task_id = input("Enter Task ID to update: ")
        task = self.find_task(task_id)
        if task:
            print(f"Current Details: {task}")
            task.title = input("Enter New Title (or press Enter to keep current): ") or task.title
            task.description = input("Enter New Description (or press Enter to keep current): ") or task.description
            task.due_date = input("Enter New Due Date (or press Enter to keep current): ") or task.due_date
            task.status = input("Enter New Status (Pending/In Progress/Completed): ") or task.status
            print("Task updated successfully!")
        else:
            print("Error: Task ID not found.")

    def delete_task(self):
        task_id = input("Enter Task ID to delete: ")
        task = self.find_task(task_id)
        if task:
            self.tasks.remove(task)
            print("Task deleted successfully!")
        else:
            print("Error: Task ID not found.")

    def filter_tasks(self):
        status = input("Enter Status to filter by (Pending/In Progress/Completed): ")
        filtered_tasks = [task for task in self.tasks if task.status == status]
        if not filtered_tasks:
            print(f"No tasks found with status '{status}'.")
        else:
            print(f"\nTasks with status '{status}':")
            for task in filtered_tasks:
                print(task)

    def save_tasks(self):
        if self.file_format == "json":
            with open(self.file_name, "w") as file:
                json.dump([task.to_dict() for task in self.tasks], file)
        elif self.file_format == "csv":
            with open(self.file_name, "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=["task_id", "title", "description", "due_date", "status"])
                writer.writeheader()
                for task in self.tasks:
                    writer.writerow(task.to_dict())
        print("Tasks saved successfully!")
        def load_tasks(self):
            try: 
              if self.file_format == "json":
                with open(self.file_name, "r") as file:
                    data = json.load(file)
                    self.tasks = [Task.from_dict(item) for item in data]
              elif self.file_format == "csv":
                with open(self.file_name, "r") as file:
                    reader = csv.DictReader(file)
                    self.tasks = [Task.from_dict(row) for row in reader]
            except FileNotFoundError:
               pass # File does not exist yet
            except Exception as e:
              print(f"Error loading tasks: {e}")

    def find_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None

    def menu(self):
        while True:
            print("\nWelcome to the To-Do Application!")
            print("1. Add a new task")
            print("2. View all tasks")
            print("3. Update a task")
            print("4. Delete a task")
            print("5. Filter tasks by status")
            print("6. Save tasks")
            print("7. Load tasks")
            print("8. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.update_task()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                self.filter_tasks()
            elif choice == "6":
                self.save_tasks()
            elif choice == "7":
                self.load_tasks()
            elif choice == "8":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


# Run the program
if __name__ == "__main__":
    manager = TaskManager()
    manager.menu()