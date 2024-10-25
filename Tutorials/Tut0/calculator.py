num1  = int(input("Enter Num1 : "))
num2  = int(input("Enter Num2 : "))


def add(x,y):
    return x + y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y=2):
    return x//y

def Calculator():
    global num1,num2
    while True:
        print("""
    Welcome to the calculator:
            options availablr:
            1. add
            2. subtarct
            3. multiply
            4. divide 
    """)
        choice = int(input("Enter you choice (1/2/3/4) : "))
        if choice == 5:
            print("Quitting the program")
            break
        if choice == 1:
            result = add(num1,num2)
            print(result)
        elif choice == 2:
            result = sub(num1,num2)
            print(result)
        elif choice == 3:
            result = mul(num1,num2)
            print(result)
        elif choice == 4:
            result = div(num1,num2)
            print(result)

        else:
            print("Invalid Choice")

# Calculator()

if __name__ == "__main__": # For Import Purpose in another file
    Calculator()