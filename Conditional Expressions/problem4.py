# Write a program to find whether a given username contains less than 10
# characters or not.

name = input("Enter username: ")

if len(name) < 10:
    print("Its less then 10")

else:
    print("Its good")