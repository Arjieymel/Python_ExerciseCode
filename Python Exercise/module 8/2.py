# Dogello, RJ-Mel B.
#BSIT 2D

#MODULE 7

#Create a class ElectricCar that inherits from the Car class. Add an additional attribute 
# battery_size to the ElectricCar class. Create an object of
#  the ElectricCar class and print its attributes.

class electric_car:
    def __init__(self,make, model, year, battery_sixe):
        self.make = make
        self.model = model
        self.year = year
        self.battery_size = battery_sixe

ElectricCar = electric_car("Tesla", "Model S", 2022, 100)

print("Output:", ElectricCar.make)
print("Output:", ElectricCar.model)
print("Output:", ElectricCar.year)
print("Output:", ElectricCar.battery_size)