f_grade = int(input("Enter 1st Grade:"))
s_grade = int(input("Enter 2nd Grade"))


if 90 <= f_grade <= 100:
    print("I got your 1st grade!")
elif 80<= s_grade <= 90:
    print("I got your 2nd grade")

grade = f_grade + s_grade

num = grade / 2


print(f"Your grade: {grade}")

print(f"your total grade: {num}")

