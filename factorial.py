#Write a python function to calculate factorial of a number (non-negative integer)

def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n! = n * (n-1)!
    return n * factorial(n-1)

num = int(input("Enter a non-negative integer: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = factorial(num)

    print("The factorial of {} is: {}".format(num, result))