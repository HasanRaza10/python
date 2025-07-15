# Create a class with a class attribute a; create an object from it and set ‘a’
# directly using ‘object.a = 0’. Does this change the class attribute?

class check:
    a = 4

b = check()
print(b.a) #its giving the class attribute 
b.a = 0 #here its assigning the value to object 
print(b.a) #giving the object value again 

# if you print class attribute it will again give you 4
print(check.a)
