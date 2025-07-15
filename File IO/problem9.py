# Write a program to find out whether a file is identical & matches the content of
# another file.

with open("this.txt") as f:
    content = f.read()

with open("log.txt") as f:
    content1 = f.read()

if (content == content1):
    print("Yes its a copy ")
else:
    print("No its not a copy")