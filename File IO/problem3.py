#  Write a program to generate multiplication tables from 2 to 20 and write it to the
# different files. Place these files in a folder for a 13 – year old.

def tablefunc(n):
    table=""
    with open (f"tables/table_{n}.txt", "w") as f:
        for i in range(1, 11):
            table +=f"{n} X {i} = {(i * n)}\n"
        f.write(table)


for i in range(2, 21):
    tablefunc(i)

