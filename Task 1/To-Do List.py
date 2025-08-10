#for storing tasks
tasks = []

#main menu
def menu():
    print("------ To-Do Lists Main Menu --------")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

#defining each menu
def view_task():
    if not tasks:
        print("There is no Tasks")
    else :
        for i, task in enumerate(tasks, start = 1):
            print(f"{i}.{task}")


