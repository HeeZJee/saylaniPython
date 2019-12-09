""" 
Answer # 1
    Write a Python function to calculate the factorial of a number (a non-negative
integer). The function accepts the number as an argument.
"""

def factorial(n):
    num = 1
    while n > 0:
        num *= n
        n -= 1
    return num

print(factorial(1))