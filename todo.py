#TASK 1
tasks = []
def display_task():
    if not tasks:
        print("No tasks available to do.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            status = "Done" if task["done"] else "Not Done"
            print(f"{i}. {task['title']} [{status}]")
def add_task():
    title = input("Enter task name: ")
    tasks.append({"title": title, "done": False})
    print("Task added successfully.")
def update_task():
    display_task()
    try:
        index = int(input("Enter task number to update: ")) - 1
        if 0 <= index < len(tasks):
            new_title = input("Enter new task name: ")
            tasks[index]["title"] = new_title
            print("Task updated successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
def delete_task():
    display_task()
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            tasks.pop(index)
            print("Task deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
def mark_completed():
    display_task()
    try:
        index = int(input("Enter task number to mark completed: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
while True:
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task Completed")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")
    if choice == "1":
        add_task()
    elif choice == "2":
        display_task()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        mark_completed()
    elif choice == "6":
        print("Exiting To-Do List. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")