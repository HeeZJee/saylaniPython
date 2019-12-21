class car():
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color
        self.seats = 7
        self.average = "12 kmpl"


car1 = car("Toyota Fortuner", 2019, "Silver")

print("Car name: {}".format(car1.name))
print("Car color: {}".format(car1.color))
print("Car model: {}".format(car1.model))
print("Car seats: {}".format(car1.seats))
print("Car average: {}".format(car1.average))
