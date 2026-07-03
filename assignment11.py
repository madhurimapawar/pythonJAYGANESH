# Assignment 11

# 1. Program to accept a number and check whether it is prime or not
def isPrime(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count = count + 1
    if count == 2:
        print(n, "is prime")
    else:
        print(n, "is not prime")

isPrime(7)


# 2. Program to accept a number and print count of digits
def countDigits(n):
    count = 0
    while n > 0:
        n = n // 10
        count = count + 1
    print(count)

countDigits(1234)


# 3. Program to accept a number and print sum of digits
def sumOfDigits(n):
    total = 0
    while n > 0:
        digit = n % 10
        total = total + digit
        n = n // 10
    print(total)

sumOfDigits(1234)


# 4. Program to accept a number and print its reverse
def reverseNumber(n):
    reverse = 0
    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10
    print(reverse)

reverseNumber(1234)


# 5. Program to accept a number and check whether it is a palindrome or not
def isPalindrome(n):
    original = n
    reverse = 0
    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10
    if original == reverse:
        print(original, "is a palindrome")
    else:
        print(original, "is not a palindrome")

isPalindrome(1221)
