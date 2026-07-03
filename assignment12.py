# Assignment 12

# 1. Program to accept a character and check whether it is a vowel or consonant
def checkVowel(ch):
    ch = ch.lower()
    if ch in "aeiou":
        print(ch, "is a vowel")
    else:
        print(ch, "is a consonant")

checkVowel('a')


# 2. Program to accept a number and print its factors
def printFactors(n):
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)

printFactors(12)


# 3. Program to accept two numbers and perform addition, subtraction, multiplication, division
def calculate(a, b):
    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    print("Division:", a / b)

calculate(10, 2)


# 4. Program to accept a number and print that many numbers starting from 1
def printNumbers(n):
    for i in range(1, n + 1):
        print(i)

printNumbers(5)


# 5. Program to accept a number and print that many numbers in reverse order
def printReverse(n):
    for i in range(n, 0, -1):
        print(i)

printReverse(5)
