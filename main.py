from manager import TaskManager
from todo import Task, PRIORITIES
from utils import validate_deadline, validate_priority

manager = TaskManager()

def menu():
    print("\n=== TO-DO LIST ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Edit Task")
    print("4. Delete Task")
    print("5. Mark Task Completed")
    print("6. Exit")
    return input("Choose an option: ")

def add_task():
    title = input("Task Title: ")
    deadline = input("Deadline (YYYY-MM-DD HH:MM): ")
    while not validate_deadline(deadline):
        print("Invalid format. Try again.")
        deadline = input("Deadline (YYYY-MM-DD HH:MM): ")

    print("\nChoose Priority:")
    for p in PRIORITIES:
        print("-", p)
    priority = input("Priority: ")
    while not validate_priority(priority):
        print("Invalid priority. Try again.")
        priority = input("Priority: ")

    task = Task(title, deadline, priority)
    manager.add_task(task)
    print("Task added!")

def view_tasks():
    tasks = manager.list_tasks()
    if not tasks:
        print("No tasks yet.")
        return

    for i, t in enumerate(tasks):
        print(f"\n[{i}] {t.title}")
        print(f" Deadline: {t.deadline}")
        print(f" Priority: {t.priority}")
        print(f" Completed: {t.completed}")

def edit_task():
    view_tasks()
    index = int(input("Choose task index to edit: "))

    new_title = input("New Title (leave blank to skip): ")
    new_deadline = input("New Deadline (YYYY-MM-DD HH:MM or blank): ")
    new_priority = input("New Priority (blank to skip): ")

    if new_deadline and not validate_deadline(new_deadline):
        print("Invalid date format.")
        return

    if new_priority and not validate_priority(new_priority):
        print("Invalid priority.")
        return

    manager.edit_task(index,
                      title=new_title or None,
                      deadline=new_deadline or None,
                      priority=new_priority or None)

    print("Task updated!")

def delete_task():
    view_tasks()
    index = int(input("Task index to delete: "))
    manager.delete_task(index)
    print("Deleted.")

def mark_done():
    view_tasks()
    index = int(input("Task index to mark as completed: "))
    manager.mark_completed(index)
    print("Marked as done!")

def main():
    while True:
        choice = menu()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            edit_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            mark_done()
        elif choice == "6":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()