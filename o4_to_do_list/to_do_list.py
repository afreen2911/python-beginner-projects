tasks=[]
print("========== TO-DO LIST ==========")

while True:
    print("1. Add Task")
    print("2. View Task")
    
    print("3. Exit")
    choice=input("Choose an option:")

    if choice=="1":
        task=input("Enter Task:")
        tasks.append(task)
        print("Tasks added!")
    elif choice=="2":
        print("Tasks:", tasks)
    elif choice=="3":
        print("Thank you for using To-Do List!")
        break


