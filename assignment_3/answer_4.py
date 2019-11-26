#Write a Python program to sum all the numeric items in a dictionary 

dic = {"Math":80,"Physics":94,"Astrophsics":88,"Programming":82}

mark = sum(dic.values())
percentage = (mark/400)*100

print("Your obtained marks is",mark,"with percentage of",percentage)

