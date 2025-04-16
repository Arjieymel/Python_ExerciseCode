# Dogello, RJ-Mel B.
#BSIT 2D

#MODULE 5

#Develop a program that prints the Fibonacci series up to 10 terms using a while loop.


first = 0
second = 1

count = 0

terms = 10

print("Fibonacci series up to 10 terms:")

while count < terms:
    print(first)
    next_term = first + second  
    first = second              
    second = next_term          
    count += 1
