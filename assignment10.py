# Assignment 10

# 1. Program to accept a number and print its multiplication table
def multiplicationTable(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num*i}")

multiplicationTable(5)


# 2. Program to accept a number and print sum of first N natural numbers
def sumOfNaturals(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i
    print(total)

sumOfNaturals(5)


# 3. Program to accept a number and print its factorial
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    print(result)

factorial(5)


# 4. Program to accept a number and print all even numbers till that number
def printEvenNumbers(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(i)

printEvenNumbers(10)


# 5. Program to accept a number and print all odd numbers till that number
def printOddNumbers(n):
    for i in range(1, n + 1):
        if i % 2 != 0:
            print(i)

printOddNumbers(10)
