#  Write a program to print third, fifth and seventh element from a list using enumerate
# function.

l = [10, 20, 30, 40, 50, 60, 70, 80, 90]

for index, value in enumerate(l):
    if index in [2, 4, 6]:
        print(value)
