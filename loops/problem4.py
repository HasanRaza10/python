# Write a program to find whether a given number is prime or not.

a = int(input("Enter a number: "))

for i in range(2, a):
    if a%i == 0:
        print("Its not prime number!")
        break

    else:
        print("Its a prime number")
        break