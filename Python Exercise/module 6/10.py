# Dogello, RJ-Mel B.
#BSIT 2D

#MODULE 6

#Write a program that defines a list of prices and calculates the total price after applying a 10% discount, 
#then prints the total price

prices = [100, 200, 150, 300]

price = sum(prices)

discount = 0.10

total = price * discount

final = price - total

print(f"List of prices: {prices}")
print(f"Total price after 10% discount: {final}")