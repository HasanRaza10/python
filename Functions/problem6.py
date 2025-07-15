# Write a python function which converts inches to cms.

# centimeters = inches * 2.54

i = int(input("Enter inches: "))
def i_to_cm(i):
    return i * 2.54

print(f"The centimeter of {i} inches is {i_to_cm(i)}")