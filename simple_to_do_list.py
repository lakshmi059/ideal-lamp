#code for simple to do list  application using python language
import json

def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)

def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task['description']} {'(Done)' if task['completed'] else ''}")

def add_task(tasks, description):
    task = {'description': description, 'completed': False}
    tasks.append(task)
    print(f"Task added: {description}")

def complete_task(tasks, index):
    if 1 <= index <= len(tasks):
        tasks[index - 1]['completed'] = True
        print(f"Task completed: {tasks[index - 1]['description']}")
    else:
        print("Invalid task index.")

def main():
    tasks = load_tasks()

    while True:
        print("\nMenu:")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            description = input("Enter task description: ")
            add_task(tasks, description)
            save_tasks(tasks)
        elif choice == '3':
            show_tasks(tasks)
            index = int(input("Enter the index of the task to mark as completed: "))
            complete_task(tasks, index)
            save_tasks(tasks)
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
