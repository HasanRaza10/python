# Write a program to find out whether a given post is talking about “Harry” or not.

post = input("Enter the post: ")

if("harry" in post.lower()):
    print("This post is talking about Harry")

else:
    print("Its not talking about Harry!")