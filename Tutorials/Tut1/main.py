# Palindrome 
def palindrom(num):

    num = str(num)

    if num == num[::-1]:
        return True
    else:
        return False
    
print(palindrom("MAM"))    


# Fibonacci series

def fibo(num):
    if num == 0:
        return 0
    elif num ==1 or num == 2:
        return 1
    else:
        return fibo(num - 1) + fibo(num - 2)

print(fibo(5))    


# 

# list1 = []
# print(list1)
# for i in range(2,13,2):
#     print(f"{i}")
#     list1.append(i)


# print(list1)


# names = []
# grades = []
# marks = []

# for i in range(5):
#     name = input("Enter Your Name : ")
#     grade = int(input("Enter Grades : "))
#     names.append(name)
#     grades.append(grade)

marks = [1,2,3,4,5]
list2 = [5,76,87]
list2.extend(marks)

print(list2.pop(1))
print(list2)



# for j in range(len(names)):
#     print(f"Name : {names[j]} and Grades : {grades[j]}")

# print(f"Name")