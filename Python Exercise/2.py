# Dogello, RJ-Mel B.
#BSIT 2D

#MODULE 2

#Python Program to Collect Personal Information

fname = input("Enter Firstname:")
mname = input("Enter Middlename:")
lname = input("Enter Lastname:")
age = int(input("Enter Age:"))
address = input("Enter Address:")
cnumber = int(input("Enter Contact Number:"))
tnumber = int(input("Enter Telephone Number:"))
email = input("Enter Email:")

print(f"Hi, my name {fname} {mname} {lname}. I am {age} years old! I live in \n {address}. if you want to contact me, my contact number is\n"
      f"{cnumber},and my telephone number is {tnumber}. \n You can reach me via email at {email}")