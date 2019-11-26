#Make a calculator using Python with addition , subtraction , multiplication , 
#division and power.


operator = input("Wanna Perform addition, subraction, multiplication, division or square? \nEnter an operator: ")
value1 = float(input("Enter first value: "))
value2 = float(input("Enter second value: "))

if operator == "add" or operator == "+":
    print("Sum of given values is: ",value1+value2)
elif operator == "minus" or operator == "-":
    print("Subraction of given values is: ",value1-value2)
elif operator == "multiply" or operator == "*":
    print("Multiplication of given values is: ",value1*value2)
elif operator == "divide" or operator == "/":
    print("Division of given values is: ",value1/value2)
elif operator == "square" or operator == "**":
    print("Square of given values is: ", value1**value2)
else:
    print("You Entered incorrect operator.")