# # Stacks Implementation


# stack = []

# def push():
#     value = int(input("Enter Value : "))
#     stack.append(value)

# def pop():
#     if is_empty():
#         print("Stack is Empty!")
#     else:
#         print(stack.pop())
#         display()

# def is_empty():
#     empty = len(stack) == 0
#     return empty

# def display():
#     if is_empty():
#         print("Stack Is Empty!")
#     else:
#         print(stack)    

# def peek():
#     if is_empty():
#         print("Stack Is Empty!")
#     else:
#         print(stack[-1])
# display()        



queue = []

def enqueue():
    value = int(input("Enter value : "))
    queue.append(value)

def is_empty():
    empty = len(queue) == 0
    return empty

def dequeue():
    if is_empty():
        print(f"Queue Is Empty : {queue}")
    else:
        queue.pop(0)
def front():
    if is_empty():            
        print(f"Queue Is Empty : {queue}")
    else:
        front = queue[0]
        print(f"The Front Value is : {front}")
def display():
    if is_empty():
        print(f"Queue Is Empty : {queue}")
    else:
        print(queue) 



# enqueue()
# enqueue()   
# enqueue()   
# dequeue()
# display()
# front()
