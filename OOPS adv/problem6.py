# Write __str__() method to print the vector as follows:
#  7i + 8j


class vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        result = vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return result
    
    def __mul__(self, other):
        result1 = self.x * other.x + self.y * other.y + self.z * other.z
        return result1
    
    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"
    
v1 = vector(1, 2, 3)
v2 = vector(4, 5, 6)
v3 = vector(7, 8, 9)

print(v1 + v2)
print(v1 * v2)

print(v2 + v3)
print(v2 * v3)