# Dogello, RJ-Mel B.
#BSIT 2D

#MODULE 7
#Define a class called Car with attributes make, model, and year. Create an object of this class and print its attributes.


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
car = Car("Toyota", "Camry", 2020)

print(car.make)
print(car.model)
print(car.year)


        