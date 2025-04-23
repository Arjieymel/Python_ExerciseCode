# Dogello, RJ-Mel B.
#BSIT 2D

#MODULE 7
#Create a function named calculate_average that takes a list of numbers as input and returns the average of those numbers.

def calculate_average(list):

    total = sum(list)

    average = total / len(list)

    return average

list = [10, 20, 30, 40, 50]

result = calculate_average(list)

print(f"the average is: {result}")
    





