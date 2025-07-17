# 1. Create a class (2-D vector) and use it to create another class representing a 3-D
# vector.

class twoDvec:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"{self.i}i + {self.j}j")

class threeDvec(twoDvec):
        def __init__(self, i, j, k):
            super().__init__(i, j)
            self.k = k

        def show1(self):
            print(f"{self.i}i + {self.j}j + {self.k}k")


twoDvec(1, 2).show()

threeDvec(1, 2, 3).show1()
