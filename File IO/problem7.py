# Write a program to find out the line number where python is present from ques 6.

line = 1
with open("log.txt") as f:
    Content = f.readline()

if "python" in Content:
    print(f"The line number is {line}")

else:
    print("There is no word as python in text")