import json
import csv

# Class to represent a task
class Task:
    def __init__(self, task_id, task_name, completed, priority):
        self.id = task_id
        self.task = task_name
        self.completed = completed
        self.priority = priority

    def __repr__(self):
        return f"Task(id={self.id}, task={self.task}, completed={self.completed}, priority={self.priority})"

# Class to manage the tasks (load, save, calculate stats)
class TaskManager:
    def __init__(self, filename):
        self.filename = filename
        self.tasks = []

    # Load tasks from JSON file
    def load_tasks(self):
        try:
            with open(self.filename, mode='r') as file:
                task_data = json.load(file)
                self.tasks = [Task(task['id'], task['task'], task['completed'], task['priority']) for task in task_data]
        except FileNotFoundError:
            print(f"Warning: The file '{self.filename}' was not found. Creating a default file...")
            self.create_default_tasks()
        except json.JSONDecodeError:
            print(f"Error: Failed to decode JSON from '{self.filename}'.")
    
    # Create a default tasks file if it's missing
    def create_default_tasks(self):
        default_tasks = [
            {"id": 1, "task": "Do laundry", "completed": False, "priority": 3},
            {"id": 2, "task": "Buy groceries", "completed": True, "priority": 2},
            {"id": 3, "task": "Finish homework", "completed": False, "priority": 1}
        ]
        self.tasks = [Task(task['id'], task['task'], task['completed'], task['priority']) for task in default_tasks]
        self.save_tasks()  # Save the default tasks to a new file
        print(f"A default 'tasks.json' file has been created with sample data.")

    # Save tasks to JSON file
    def save_tasks(self):
        try:
            with open(self.filename, mode='w') as file:
                task_data = [{
                    'id': task.id,
                    'task': task.task,
                    'completed': task.completed,
                    'priority': task.priority
                } for task in self.tasks]
                json.dump(task_data, file, indent=4)
        except Exception as e:
            print(f"Error: Unable to save to '{self.filename}': {e}")

    # Display all tasks
    def display_tasks(self):
        print("ID\tTask Name\t\tCompleted\tPriority")
        print("-" * 50)
        for task in self.tasks:
            print(f"{task.id}\t{task.task}\t\t{task.completed}\t\t{task.priority}")

    # Calculate and display task stats
    def calculate_task_stats(self):
        total_tasks = len(self.tasks)
        completed_tasks = len([task for task in self.tasks if task.completed])
        pending_tasks = total_tasks - completed_tasks
        average_priority = sum(task.priority for task in self.tasks) / total_tasks if total_tasks > 0 else 0

        print("\nTask Completion Stats:")
        print(f"Total tasks: {total_tasks}")
        print(f"Completed tasks: {completed_tasks}")
        print(f"Pending tasks: {pending_tasks}")
        print(f"Average priority: {average_priority:.2f}")

    # Convert tasks to CSV
    def convert_to_csv(self, csv_file_name):
        try:
            with open(csv_file_name, mode='w', newline='') as file:
                fieldnames = ['ID', 'Task', 'Completed', 'Priority']
                csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
                csv_writer.writeheader()
                for task in self.tasks:
                    csv_writer.writerow({
                        'ID': task.id,
                        'Task': task.task,
                        'Completed': task.completed,
                        'Priority': task.priority
                    })
            print(f"\nTasks have been successfully converted to '{csv_file_name}'.")
        except Exception as e:
            print(f"Error: Unable to convert to CSV: {e}")

# Main function
def main():
    tasks_file = 'tasks.json'

    # Create TaskManager object
    task_manager = TaskManager(tasks_file)

    # Load tasks from JSON file
    task_manager.load_tasks()

    # Only proceed if tasks were successfully loaded
    if task_manager.tasks:
        # Display all tasks
        task_manager.display_tasks()

        # Calculate and display task completion stats
        task_manager.calculate_task_stats()

        # Convert tasks to CSV
        task_manager.convert_to_csv('tasks.csv')

        # Modify a task (mark the first task as completed)
        task_manager.tasks[0].completed = True

        # Save changes back to the JSON file
        task_manager.save_tasks()
        print(f"\nChanges have been saved to '{tasks_file}'.")

if __name__ == "__main__":
    main()
