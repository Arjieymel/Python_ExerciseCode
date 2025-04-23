# Dogello, RJ-Mel B.
#BSIT 2D

#MODULE 7
#Write a function named reverse_string that takes a string as input and returns the reversed version of the string.

def reversed_string(words):

    rev = ''.join(reversed(words))

    return rev

result = reversed_string("hello")


print(f"Output:{result}")
