# Write a python program using function to convert Celsius to Fahrenheit.

# c = 5*(f - 32)/9

c = int(input("Enter temp in celsius: "))

def celTofar(c):
    f = ((c * 9)/5) + 32
    return f

f = celTofar(c)

print(f"The celsius {c} in fahrenheit is {round(f, 2)}")
