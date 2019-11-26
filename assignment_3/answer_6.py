#Write a Python script to check if a given key already exists in a dictionary 

dic = {"Student1":"Hafeez","Student2":"Sameer","Student3":"Asad","Student4":"Mehmood","Student5":"Hamza"}
duplicate = {}
print(dic)
key = "Student1"
if key in dic.keys(): 
        print(key," is present and his name is ",dic[key])
else:
        print("Not present")