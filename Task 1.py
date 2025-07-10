# TO DO LIST
todo_list = []
def show_menu():
    print("\n-To-Do List Menu -")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as completed")
    print("4. Delete task")
    print("5. Exit")
def view_tasks():
    if len(todo_list) == 0:
        print("Your to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for i in range(len(todo_list)):
            task = todo_list[i]
            if task['completed']:
                status = "✓"
            else:
                status = "✗"
            print(f"{i + 1}. {task['task']} [{status}]")
def add_task():
    task_name = input("Enter a new task: ")
    task = {
        'task': task_name,
        'completed': False
    }
    todo_list.append(task)
    print("Task added successfully!")
def mark_completed():
    view_tasks()
    try:
        task_num = int(input("Enter the number of the task you completed: "))
        if task_num >= 1 and task_num <= len(todo_list):
            todo_list[task_num - 1]['completed'] = True
            print("Task marked as completed!")
        else:
            print("That task number doesn't exist.")
    except:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter the number of the task to delete: "))
        if task_num >= 1 and task_num <= len(todo_list):
            removed_task = todo_list.pop(task_num - 1)
            print(f"Deleted task: {removed_task['task']}")
        else:
            print("That task number doesn't exist.")
    except:
        print("Please enter a valid number.")

while True:
    show_menu()
    user_choice = input("Choose an option (1 to 5): ")

    if user_choice == '1':
        view_tasks()
    elif user_choice == '2':
        add_task()
    elif user_choice == '3':
        mark_completed()
    elif user_choice == '4':
        delete_task()
    elif user_choice == '5':
        print("Thanks for using the To-Do List. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
