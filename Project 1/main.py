#                         PROJECT 1: SNAKE, WATER, GUN GAME

# We all have played snake, water gun game in our childhood. If you haven’t, google the
# rules of this game and write a python program capable of playing this game with the
# user.

import random

computer = random.choice([-1, 0, 1])

word = input(''' Enter the your choice: 
w for water, s for snake, g for gun    -> ''')

dict = {"s": -1, "w": 0, "g": 1}

revDict = {-1: "snake", 0: "water", 1: "gun"}

user = dict[word]

if (user == computer):
    print("Its a Draw")

elif (computer == -1 and user == 0):
    print("You Lost!")

elif (computer == -1 and user == 1):
    print("You Won")

elif (computer == 0 and user == -1): 
    print("You Won!")

elif (computer == 0 and user == 1):
    print("You Lost!")

elif (computer == 1 and user == -1):
    print("You Lost!")

elif (computer == 1 and user == 0):
    print("You Won!")

else:
    print("Invalid Input!")

print(f"You choosed {revDict[user]}")
print(f"Compuer choosed {revDict[computer]}")