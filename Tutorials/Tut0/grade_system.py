"""QUIZ : Write a program to find out even and odd numbers using functions and conditional statements 
"""


# def summation(*args):
#     return sum(args)

# print(summation(1,2,3,4))

# add = lambda x,y: x + y


# def main(add):
#     print(add)

# main(add(2,5))


def factorial(n):
    """THIS FUCTION CALCULATES FACTORIALS
    """
    # 
    if n == 0:
        return 1
    else:
        f = n * factorial(n-1)
        return f




def factor(func,value):
    print(func(value))

factor(factorial,5)
print(factorial.__doc__)

