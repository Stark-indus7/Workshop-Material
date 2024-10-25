# tasks = []

# def add_tasks():
#     task = input("Enter Your task : ")
#     tasks.append(task)

# def show_tasks():
#     if not tasks:
#         print("No tasks Present!")
#     else:
#         for i in tasks:
#             print(i)

# def remove_tasks():
#     if not tasks:
#         print("No Tasks Present!")
#     else:
#         show_tasks()
#         search = int(input("Enter the Number of tasks : "))
#         print(tasks.pop(search-1))

# def clear_task():
#     if not tasks:
#         print("No Tasks Present!")
#     else:
#         tasks.clear()    
# def todo():
#     print("""Welcome to personal to-do:
#           options available:
#           1. Add Task
#           2. Show tasks
#           3. Remove Tasks
#           4. clear all tasks
#           5. Quit""")
#     while True:
#         iccha  = int(input("Enter Your Iccha : "))
#         if iccha == 5:
#             print("Bye Bye")
#             break
#         if iccha == 1:
#             add_tasks()
#         elif iccha == 2:
#             show_tasks()
#         elif iccha == 3:
#             remove_tasks()
#         elif iccha == 4:
#             clear_task()    
#         else:
#             print("Invalid Iccha! Soch Samjh ke Daale")            

# todo()






profile = {"name" : "apoorav","age":20}
print(profile)

profile["name"] = "shyam"
print(profile)