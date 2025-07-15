# Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.

mark1 = int(input("Enter the mark of sub 1: "))
mark2 = int(input("Enter the mark of sub 2: "))
mark3 = int(input("Enter the mark of sub 3: "))

percentage = ((mark1 + mark2 + mark3) /300) * 100

mark1_per = (mark1/100) * 100
mark2_per = (mark2/100) * 100
mark3_per = (mark3/100) * 100

if (mark1_per >= 33 and mark2_per >= 33 and mark3_per >= 33 and percentage >= 40 ):
    print("Congrats you passed and you total percentage is", percentage)

else:
    print("You failed try next time and total percentage is", percentage)


