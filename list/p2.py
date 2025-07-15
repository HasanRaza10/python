#  Write a program to accept marks of 6 students and display them in a sorted
# manner.

marks = []

for  i in range(6):
    a = int(input(f"Enter a marks student {i + 1}: "))
    marks.append(a)

marks.sort()

print(marks)