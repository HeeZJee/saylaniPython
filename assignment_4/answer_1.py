"""Use a dictionary to store information about a person you know. Store their first name, last name, age, and the city in which they live. You should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary. Add a new key value pair about qualification then update the qualification value to high academic level then delete it.
"""

bio = { 
"first_name":"Hafeez",
"last_name": "Ghanchi",
"age": "21",
"city": "Karachi"}

for x in bio.items():
    print(x)
print('\n')

bio.update({"qualification":"High Academic Level"})
for x in bio.items():
    print(x)
print('\n')

bio.pop("qualification")
for x in bio.items():
    print(x)
print('\n')