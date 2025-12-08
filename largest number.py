a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a > b:
    if a > c:
        print(a, "is the largest.")
    else:
        print(c, "is the largest.")
else:
    if b > c:
        print(b, "is the largest.")
    else:
        print(c, "is the largest.")