# Lista donde se guardan las tareas
tasks = []


# -------------------------
# FUNCIONES
# -------------------------

def add_task():
    print("\n--- Add Task ---")

    task_id = input("Enter ID: ")
    title = input("Enter title: ")
    description = input("Enter description: ")
    priority = input("Enter priority (high, medium, low): ")
    status = "pending"

    task = {
        "id": task_id,
        "title": title,
        "description": description,
        "priority": priority,
        "status": status
    }

    tasks.append(task)
    print("Task added successfully!")


def show_tasks():
    print("\n--- Task List ---")

    if len(tasks) == 0:
        print("No tasks available.")
        return

    for task in tasks:
        print(task)


def find_task():
    print("\n--- Find Task ---")

    search_id = input("Enter task ID: ")

    for task in tasks:
        if task["id"] == search_id:
            print("Task found:")
            print(task)
            return

    print("Task not found.")


def update_task():
    print("\n--- Update Task ---")

    search_id = input("Enter task ID: ")

    for task in tasks:
        if task["id"] == search_id:
            task["title"] = input("New title: ")
            task["description"] = input("New description: ")
            task["priority"] = input("New priority: ")
            task["status"] = input("New status (pending/completed): ")

            print("Task updated successfully!")
            return

    print("Task not found.")


def delete_task():
    print("\n--- Delete Task ---")

    search_id = input("Enter task ID: ")

    for task in tasks:
        if task["id"] == search_id:
            tasks.remove(task)
            print("Task deleted successfully!")
            return

    print("Task not found.")


def menu():
    print("\n===== TASK MANAGER =====")
    print("1. Add task")
    print("2. Show tasks")
    print("3. Find task")
    print("4. Update task")
    print("5. Delete task")
    print("6. Exit")


# -------------------------
# PROGRAMA PRINCIPAL
# -------------------------

option = 0

while option != 6:
    menu()
    
    try:
        option = int(input("Choose an option: "))
    except:
        print("Invalid input")
        continue

    if option == 1:
        add_task()
    elif option == 2:
        show_tasks()
    elif option == 3:
        find_task()
    elif option == 4:
        update_task()
    elif option == 5:
        delete_task()
    elif option == 6:
        print("Goodbye!")
    else:
        print("Invalid option")
