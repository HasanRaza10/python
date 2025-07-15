# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)
# and get fare information of train running under Indian Railways.


from random import randint
class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo
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
