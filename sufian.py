
tasks = []

def show_tasks():
    if len(tasks) == 0:
        print("\nNo tasks added yet.")
    else:
        print("\n------ YOUR TASKS ------")
        for i in range(len(tasks)):
            print(i + 1, ".", tasks[i])

while True:
    print("\n========================")
    print("     DAILY TASK TRACKER")
    print("========================")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Complete a task")
    print("4. Delete a task")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        task = input("Enter your new task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        show_tasks()

        if len(tasks) > 0:
            number = int(input("Enter task number to complete: "))

            if number >= 1 and number <= len(tasks):
                tasks[number - 1] = tasks[number - 1] + " [Completed]"
                print("Task completed!")
            else:
                print("Invalid task number.")

    elif choice == "4":
        show_tasks()

        if len(tasks) > 0:
            number = int(input("Enter task number to delete: "))

            if number >= 1 and number <= len(tasks):
                tasks.pop(number - 1)
                print("Task deleted successfully!")
            else:
                print("Invalid task number.")

    elif choice == "5":
        print("Thank you for using Daily Task Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")
