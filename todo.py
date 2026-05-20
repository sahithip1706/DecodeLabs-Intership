tasks = []
task_id = 1

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter task: ")

        task = {
            "id": task_id,
            "name": name
        }

        tasks.append(task)
        task_id += 1

    elif choice == "2":
        print("\nYour Tasks:")
        for t in tasks:
            print(t["id"], "-", t["name"])

    elif choice == "3":
        break

    else:
        print("Invalid choice")


        