def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

def factorial_iterative(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

n = int(input("Enter n for factorial: "))
print("Recursive:", factorial_recursive(n))
print("Iterative:", factorial_iterative(n))
