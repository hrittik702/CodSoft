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
        print("There is no Task")
    else :
        for i, task in enumerate(tasks, start = 1):
            print(f"{i}. {task}")

def add_task():
    new_task = input("New Task : ")
    tasks.append(new_task)

def mark_task():
    if not tasks:
        print("Please, Add a Task First")
    else:
        view_task()
        mark = input("Enter Task No. to mark Completed")
        tasks[mark-1] = tasks[mark-1] + " ✅"
        print("Task marked as Completed")


#working function
while True :
    print("\n")
    menu()
    user_choice = input("Choose an Option : ")

    if user_choice=='1':
        view_task()
    elif user_choice=='2':
        add_task()
    elif user_choice=='5':
        print("User Exits")
        break
    else :
        print("Invalid User Choice, Enter a Valid Option")


