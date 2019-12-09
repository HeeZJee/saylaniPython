"""
Answer # 5
Write a Python function that takes a number as a parameter and check the
number is prime or not.
"""

def isprime():
    nums = int(input("Enter any number to check if it is prime or not: "))
    return prime(nums)

def prime(nums):
    if nums > 1:
        for num in range(2,nums):
            if (nums % num) == 0:
                print("It is not a prime number.")
                print(num,"times",nums//num, "is", nums)
                break
        else:
            print("It is a prime number.")

isprime()