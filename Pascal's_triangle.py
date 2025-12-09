import math

rows = int(input("Enter number of rows: "))

for i in range(rows):
    # for spacing
    for space in range(rows - i):
        print(" ", end=" ")
    
    # print numbers
    for j in range(i + 1):
        value = math.factorial(i) // (math.factorial(j) * math.factorial(i - j))
        print(value, end="   ")
    
    print()