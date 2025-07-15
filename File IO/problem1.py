# Write a program to read the text from a given file ‘poems.txt’ and find out
# whether it contains the word ‘twinkle’.

with open("poems.txt") as f:
    poem = f.read()
    if "twinkle" in poem:
        print("Twinkle is present in poem")

    else:
        print("Twinkle is not Present in poem")

