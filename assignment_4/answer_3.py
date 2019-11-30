"""A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their age, and then tell them the cost of their movie ticket."""

while True:
    age = int(input("Enter Your Age: \nPress '0' to exit.\n"))
    if age == 0:
        break
    if age <= 3:
        print("Your ticket is free.\n")
    elif age <= 12 and age >= 4:
        print("The cost of your ticket is $10.\n")
    elif age > 12 and age <= 120:
        print("The cost of your ticket is $15.\n")
    else:
        print("Invalid input! Enter correct age.\n")
    
