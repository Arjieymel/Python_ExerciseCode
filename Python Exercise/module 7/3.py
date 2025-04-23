# Dogello, RJ-Mel B.
#BSIT 2D

#MODULE 7
#Develop a program that reads a list of numbers and calculates the sum of all numbers in the list, then prints the sum.


input_str = input("Enter numbers separated by spaces: ")

numbers = list(map(int, input_str.split()))

total_sum = sum(numbers)

print("The sum of the numbers is:", total_sum)

