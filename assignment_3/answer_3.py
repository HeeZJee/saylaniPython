#Write a Python script to add a key to a dictionary 

print("\nCurrent Dictionary is;")
dic = {"University":"University of Karachi","Department":"Institute of Space Science and Technology","Batch":2019,"Student Name":"Hafeez Ghanchi"}
print(dic)

print("\nUpdated Dictionary is;")
new_dic = {"Student ID":"EH1918015","Major":"Astrophysics"}
dic.update(new_dic)
print(dic)