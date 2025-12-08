n = int(input("Enter value of N: "))

i = 1
total = 0

print("First", n, "natural numbers:")

while i <= n:
    print(i)
    total += i
    i += 1

print("Sum =", total)