# Write a program to mine a log file and find out whether it contains ‘python’.

with open("file.txt") as f:
    Content = f.read()

if "python" in Content:
    print("There is python word in text")

else:
    print("There is no word as python in text")