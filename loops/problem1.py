# Write a program to print multiplication table of a given number using for loop.

a = int(input("Enter number: "))

for i in range(1, 11):
    print(f"{a} X {i} = {a * i}")