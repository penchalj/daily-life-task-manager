import sys

# The global list that will hold task dictionaries
# Example task: {"task": "Clean room", "completed": False, "priority": "Medium"}
tasks = []

def show_menu():
    print("\n--- DAILY LIFE TASK MANAGER ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Exit")

def view_tasks():
    if not tasks:
        print("\nYour list is empty!")
    else:
        for index, t in enumerate(tasks):
            status = "[X]" if t.get("completed") else "[ ]"
            print(f"{index}. {status} {t['task']}")

def add_task():
    name = input("Enter task description: ")
    tasks.append({"task": name, "completed": False})
    print("Task added!")

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
