# Assignment 13

# 1. Program to accept length and width of a rectangle and print area
def rectangleArea(length, width):
    area = length * width
    print(area)

rectangleArea(5, 3)


# 2. Program to accept radius of a circle and print area
def circleArea(radius):
    area = 3.14 * radius * radius
    print(area)

circleArea(5)


# 3. Program to accept a number and check whether it is a perfect number or not
def isPerfect(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total = total + i
    if total == n:
        print(n, "is a perfect number")
    else:
        print(n, "is not a perfect number")

isPerfect(28)


# 4. Program to accept a number and print its binary equivalent
def toBinary(n):
    binary = ""
    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n = n // 2
    print(binary)

toBinary(10)


# 5. Program to accept marks and display grade
# >=75 Distinction, >=60 First Class, >=50 Second Class, <50 Fail
def displayGrade(marks):
    if marks >= 75:
        print("Distinction")
    elif marks >= 60:
        print("First Class")
    elif marks >= 50:
        print("Second Class")
    else:
        print("Fail")

displayGrade(80)
