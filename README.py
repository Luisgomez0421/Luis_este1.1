import json

FILE = "tasks.json"
tasks = []


# -------------------------
# LOAD & SAVE
# -------------------------

def load_tasks():
    global tasks

    try:
        with open(FILE, "r", encoding="utf-8") as file:
            tasks = json.load(file)
    except:
        tasks = []


def save_tasks():
    with open(FILE, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)


# -------------------------
# ID GENERATOR
# -------------------------

def generate_id():
    if len(tasks) == 0:
        return 1
    
    max_id = 0
    for task in tasks:
        if task["id"] > max_id:
            max_id = task["id"]
    
    return max_id + 1


# -------------------------
# VALIDATIONS
# -------------------------

def validate_priority(priority):
    return priority in ["high", "medium", "low"]


def validate_status(status):
    return status in ["pending", "completed"]


# -------------------------
# FUNCTIONS
# -------------------------

def add_task():
    print("\n--- Add Task ---")

    title = input("Enter title: ")
    description = input("Enter description: ")

    priority = input("Enter priority (high, medium, low): ")
    if not validate_priority(priority):
        print("Invalid priority")
        return

    task = {
        "id": generate_id(),
        "title": title,
        "description": description,
        "priority": priority,
        "status": "pending"
    }

    tasks.append(task)
    save_tasks()
    print("Task added successfully!")


def show_tasks():
    print("\n--- Task List ---")

    if len(tasks) == 0:
        print("No tasks available.")
        return

    for task in tasks:
        print("ID:", task["id"])
        print("Title:", task["title"])
        print("Description:", task["description"])
        print("Priority:", task["priority"])
        print("Status:", task["status"])
        print("-------------------------")


def find_task():
    print("\n--- Find Task ---")
    print("1. Search by ID")
    print("2. Search by title")
    print("3. Search by status")

    option = input("Choose option: ")

    if option == "1":
        try:
            search_id = int(input("Enter ID: "))
        except:
            print("Invalid ID")
            return

        for task in tasks:
            if task["id"] == search_id:
                print(task)
                return

        print("Task not found.")

    elif option == "2":
        title = input("Enter title: ").lower()
        found = False

        for task in tasks:
            if title in task["title"].lower():
                print(task)
                found = True

        if not found:
            print("No tasks found.")

    elif option == "3":
        status = input("Enter status (pending/completed): ")

        if not validate_status(status):
            print("Invalid status")
            return

        found = False

        for task in tasks:
            if task["status"] == status:
                print(task)
                found = True

        if not found:
            print("No tasks found.")

    else:
        print("Invalid option")


def update_task():
    print("\n--- Update Task ---")

    try:
        search_id = int(input("Enter ID: "))
    except:
        print("Invalid ID")
        return

    for task in tasks:
        if task["id"] == search_id:

            title = input("New title: ")
            description = input("New description: ")
            priority = input("New priority: ")
            status = input("New status: ")

            if not validate_priority(priority) or not validate_status(status):
                print("Invalid data")
                return

            task["title"] = title
            task["description"] = description
            task["priority"] = priority
            task["status"] = status

            save_tasks()
            print("Task updated successfully!")
            return

    print("Task not found.")


def delete_task():
    print("\n--- Delete Task ---")

    try:
        search_id = int(input("Enter ID: "))
    except:
        print("Invalid ID")
        return

    for task in tasks:
        if task["id"] == search_id:
            tasks.remove(task)
            save_tasks()
            print("Task deleted successfully!")
            return

    print("Task not found.")


def menu():
    print("""
===== TASK MANAGER =====
1. Add task
2. Show tasks
3. Find task
4. Update task
5. Delete task
6. Exit
""")


# -------------------------
# MAIN
# -------------------------

load_tasks()

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
