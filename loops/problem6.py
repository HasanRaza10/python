# Write a program to calculate the factorial of a given number using for loop.

n = int(input("Enter the number: "))
factorial = 1

for i in range(n):
    factorial = factorial * (n - i)

print(f"The factorial of {n} is {factorial}")
