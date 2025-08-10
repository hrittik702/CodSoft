# Simple To-Do List Demo (For Learning Purpose Only)

tasks = []  # Stores tasks as strings

def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added!")

def mark_completed():
    view_tasks()
    try:
        num = int(input("Enter task number to mark completed: "))
        tasks[num - 1] = tasks[num - 1] + " ✅"
        print("Task marked as completed.")
    except (IndexError, ValueError):
        print("Invalid task number.")

def delete_task():
    view_tasks()
    try:
        num = int(input("Enter task number to delete: "))
        deleted = tasks.pop(num - 1)
        print(f"Task '{deleted}' deleted.")
    except (IndexError, ValueError):
        print("Invalid task number.")

# Main program loop
while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        mark_completed()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
