# Write a program to display a/b where a and b are integers. If b=0, display infinite by
# handling the ‘ZeroDivisionError’.



try:
    a = int(input("Enter the a value: "))
    b = int(input("Enter the b value: "))

    print(a/b)


except Exception as ZeroDivisionError:
        print("Infinity")
