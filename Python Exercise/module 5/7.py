# Dogello, RJ-Mel B.
#BSIT 2D

#MODULE 5

#Write a program that prints numbers from 1 to 10 but skips 5 using a while loop.

num = 1

while num <= 10:
    if num == 5:
        num += 1  
        continue
    print(num)
    num += 1
