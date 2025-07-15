#  Can you change the self-parameter inside a class to something else (say
# “harry”). Try changing self to “slf” or “harry” and see the effects.

#The Answer is it will work without any issues we can use whatever instead of "self" but
#it reduces the readablity of program so better to avoid such things

from random import randint
class Train:
    def __init__(harry, trainNo):
        harry.trainNo = trainNo
    def bookTicket(self, fro, to):
        print(f"Your train is booked and Train No is {self.trainNo} from {fro} to {to} ")

    def getFare(self):
        print(f"Train no {self.trainNo} is running on Time!")

    def getStatus(self, fro, to):
        print(f"Train from {fro} to {to} with train no: {self.trainNo} and your ticket no is {randint(222, 555)}")

a = Train(12249)
a.bookTicket("shimoga", "Banglore")
a.getFare()
a.getStatus("shimoga", "Banglore")
