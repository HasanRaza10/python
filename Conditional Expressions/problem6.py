# Write a program to calculate the grade of a student from his marks from the
# following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50 => F

mark = int(input("Enter marks: "))

if (mark >= 90):
    grade = "Ex"

elif(mark >= 80 and mark < 90):
    grade = "A"

elif(mark >= 70 and mark < 80):
    grade = "B"

elif(mark >= 60 and mark < 70):
    grade = "C"

elif(mark >= 50 and mark < 60):
    grade = "D"

elif(mark < 50):
    grade = "F"

print(f"{mark}-> {grade}")