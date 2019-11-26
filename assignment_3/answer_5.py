#Write a program to identify duplicate values from list 

list = ["Hammer",24,.75,"Cow",3e8,"Hammer",50,.75,"Beast","Beast",3e8]
duplicate = []
for i in range(len(list)):
    inc = i+1
    for j in range(inc,len(list)):
        if list[i] == list[j] and list[i] not in duplicate:
            duplicate.append(list[i])
print("Duplicate values from a list is: ",duplicate)            