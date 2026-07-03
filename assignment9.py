# Assignment 9

# 1. Program with one function Display() that prints "jay ganesh" on console
def Display():
    print("jay ganesh")

Display()


# 2. Program with function chkgreater() that accepts two numbers and prints the greater one
def chkgreater(a, b):
    if a > b:
        print(a)
    else:
        print(b)

chkgreater(10, 20)


# 3. Program to accept a number and print its square
def square(num):
    print(num ** 2)

square(5)


# 4. Program to accept a number and print its cube
def sqr(a):
    print(a * a * a)

sqr(5)


# 5. Program to accept a number and check whether it is divisible by 3 and 5
def checkDivisible(num):
    if num % 3 == 0 and num % 5 == 0:
        print("divisible by 3 and 5")
    elif num % 3 == 0:
        print("divisible by 3")
    elif num % 5 == 0:
        print("divisible by 5")
    else:
        print("not divisible by 3 or 5")

checkDivisible(15)
