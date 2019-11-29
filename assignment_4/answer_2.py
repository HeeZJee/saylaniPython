"""Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city. The keys for each city’s dictionary should be something like country, population, and fact. Print the name of each city and all of the information you have stored about it."""

cities = {"Karachi"
:{"Country":"Pakistan"
,"Population":"15,741,406"
,"GDP":"$114 billion"
},
"Mumbai":
{"Country":"India"
,"Population":"12,478,447"
,"GDP":" $368 billion"
},
"New York City"
:{"Country":"United States of America (USA)"
,"Population":"8,175,133"
,"GDP":"$1550 billion "
}
}

for city in cities.keys():
    print(city)
    print(cities[city])
    print("\n")
