def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    power = len(digits)
    return sum(d**power for d in digits) == n

armstrongs = [i for i in range(1, 1001) if is_armstrong(i)]
print("Armstrong numbers (1..1000):", armstrongs)
