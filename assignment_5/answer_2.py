"""
Answer # 2
    Write a Python function that accepts a string and calculate the number of upper
case letters and lower case letters.
"""

def caseCLC(string):
    uppers = 0
    lowers = 0
    for char in string:
        if char.islower():
            lowers += 1
        elif char.isupper():
            uppers += 1
    return uppers, lowers

print(caseCLC("Hello Hafeez Ghanchi! are you ready to be called as Microsoft Certified Python Developer after 14 December?"))