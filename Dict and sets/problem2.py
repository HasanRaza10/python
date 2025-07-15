# Write a program to input eight numbers from the user and display all the unique
# numbers (once).

# list =[]
# for i in range(8):
#     a = int(input("Enter the number: "))
#     list.append(a)

# print(list)



s =set()

for i in range(8):
    a = int(input("Enter the number: "))
    s.add(a)

print(s)