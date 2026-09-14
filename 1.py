# write a python program to define a method factorial that has 1 parameter and return the result after computing the factorial of the given number

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

x = int(input("Enter the Number:"))
y = factorial(x)
print(y)
