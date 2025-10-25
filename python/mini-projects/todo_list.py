# Task list
task = []

# add task 
def addTasks(*taskss):
    # taskss = list(taskss)
    for index, i in enumerate(taskss):
        task.append([taskss[index],"[ ]"])


# view task
def viewTask():
    if len(task) == 0:
        print("Tasks".center(45,"~"))
        print("There is no any task added.")
    else:
        print("Tasks".center(45,"~"))
        for i, t in enumerate(task):
            print(f"{i + 1}. {t[0]} {t[1]}")

# delete task uses index number to delete task
def delTask(i):
    task.remove(task[i-1])

# Task completion
def taskComplete(i):
    task[i-1][1] = "✅"
    print(f"Task\n{i}. {task[i-1][0]} {task[i-1][1]}")


while True:
    prompt = input("Add task(press 'q' to quit): ")
    if prompt == "q":
        print("Exiting...... Task CLI")
        break
    elif prompt == "tasks":  # View tasks
        viewTask()
    
    elif prompt == "remove": # Remove tasks
        l = []
        viewTask()
        sno = input("Enter the serial number of the task: ")
        sno = sno.split(",")
        for i in sno:
            l.append(int(i))
        l.sort()
        for index, i in enumerate(l):
            delTask(i-index)
            print(f"Task number {i} is removed form the list.")
        
    elif prompt == "complete":
        l = []
        viewTask()
        sno = input("Enter the serial number of the task: ").split(",")
        for i in sno:
            l.append(int(i))
        for t in l:
            taskComplete(t)

    elif isinstance(prompt, str):  # Add tasks
        prompt = prompt.split(",")
        for t in prompt:
            addTasks(t)
        for i in prompt:
            print(f"{i} is added to tasks list.")
    
    
# addTasks("homework","gym")
# viewTask()




# addTasks("Gym Workout","Homework","Do some programming","Breath air")
# viewTask()
# taskComplete(4)
# viewTask()
# delTask(4)
# viewTask()