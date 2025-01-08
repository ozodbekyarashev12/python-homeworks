import json
import csv

# Step 1: Create the tasks.json file
tasks_data = [
    {"id": 1, "task": "Do laundry", "completed": False, "priority": 3},
    {"id": 2, "task": "Buy groceries", "completed": True, "priority": 2},
    {"id": 3, "task": "Finish homework", "completed": False, "priority": 1},
]

tasks_json_path = "tasks.json"
tasks_csv_path = "tasks.csv"

# Writing initial tasks data to the JSON file
with open(tasks_json_path, mode="w") as file:
    json.dump(tasks_data, file, indent=4)


# Step 2: Load and display tasks from tasks.json
def load_tasks(json_path):
    with open(json_path, mode="r") as file:
        return json.load(file)


def display_tasks(tasks):
    print("ID\tTask Name\t\tCompleted\tPriority")
    for task in tasks:
        print(f"{task['id']}\t{task['task']}\t{task['completed']}\t{task['priority']}")


# Step 3: Save tasks back to tasks.json
def save_tasks(tasks, json_path):
    with open(json_path, mode="w") as file:
        json.dump(tasks, file, indent=4)


# Step 4: Calculate task completion stats
def calculate_stats(tasks):
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task["completed"])
    pending_tasks = total_tasks - completed_tasks
    average_priority = sum(task["priority"] for task in tasks) / total_tasks

    return {
        "Total Tasks": total_tasks,
        "Completed Tasks": completed_tasks,
        "Pending Tasks": pending_tasks,
        "Average Priority": average_priority,
    }


# Step 5: Convert tasks to tasks.csv
def convert_to_csv(tasks, csv_path):
    with open(csv_path, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["ID", "Task", "Completed", "Priority"])
        writer.writeheader()
        for task in tasks:
            writer.writerow(
                {
                    "ID": task["id"],
                    "Task": task["task"],
                    "Completed": task["completed"],
                    "Priority": task["priority"],
                }
            )


# Execute the steps
tasks = load_tasks(tasks_json_path)
display_tasks(tasks)
stats = calculate_stats(tasks)
print("\nTask Completion Stats:")
for key, value in stats.items():
    print(f"{key}: {value}")

# Save tasks (no modifications made here, but the function works for updates)
save_tasks(tasks, tasks_json_path)

# Convert tasks to CSV
convert_to_csv(tasks, tasks_csv_path)