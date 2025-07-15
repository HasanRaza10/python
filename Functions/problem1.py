#  Write a program using functions to find greatest of three numbers

a = 10
b = 24
c = 17

def greatest(a, b, c):
    if (a > b) and (a > c):
        return a
    elif (b > a) and (b > c):
        return b
    else:
        return c
    
print(greatest(a, b, c))
