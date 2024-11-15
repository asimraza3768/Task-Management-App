# creating a function task to make a app
def task():
    
    tasks = [] # creating list to add task in it.
    print("---Welcome to task management app---")

    while True:  # start an infinity loop to continously promt the user till he entered valid number
        try:
            total_task = int(input("Enter how many task you want to add: ")) # asking how many task you want to add

            # checking if the entered number is less than or equal to zero.
            if total_task <=0:
                print("Please enter a positive number!")
                
            else:
                print(f"Great! You want to add {total_task} tasks.")
                break

        # if user input is invalid it will inform the user/.
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            
    
    # creating for loop to add task one by one
    for i in range(1,total_task+1):
        task_name = input(f"Enter task {i}: ")
        tasks.append(task_name)
    
    # printing all tasks that has been added
    print(f"Todays task are {tasks}")

    # creating while loop to add,update,delete,view the task and to exit the app.
    while True:
        operation = int(input("Enter 1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop"))

        # using if-elif to add,update,delete,view the task and to exit the app.

        # adding task
        if operation == 1:
            add = input("Enter task you want to add: ")
            tasks.append(add)

        # Updating task
        elif operation == 2:
            while True:
                old_task = input("Enter the task you want to update (or enter \"exit\" to cancel): ")

                if old_task.lower() == "exit":
                    print("Update opereation canceled!")

                if old_task in tasks:
                    updated = input("Enter new task: ")
                    ind = tasks.index(old_task)
                    tasks[ind] = updated
                    print(f"Updated tasks: {tasks}")
                    break

                else:
                    print(f"Task {old_task} has not found")




        # Deleting task
        elif operation == 3:
            while True:
                del_task = input("Enter task you want to delete (or enter \"exit\" to cancel): ")
                if del_task.lower() == "exit":
                    print("Update opereation canceled!")
                    break

                if del_task in tasks:
                    ind = tasks.index(del_task)
                    del tasks[ind]

                    print(f"Task {del_task} has been deleted.")
                    break

                else:
                    print(f"Task {del_task} has not found")

        # Viewing task
        elif operation == 4:
            print(f" Total tasks {tasks}")

        # closing the program
        elif operation == 5:
            print("CLosing....")
            break
        else:
            print("Invalid input!")

task()