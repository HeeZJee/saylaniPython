#Write a program to check if there is any numeric #value in list using for loop 


list = ["Cat",2,"Boy",5,6.,"Pen",7.6,False,None,3e8]
for i in range(0,len(list)):
        if type(list[i]) == float or type(list[i]) == int:
            numeric = print("Numeric values from the list is: ",list[i])