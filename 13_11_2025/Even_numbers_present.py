def count_evens(lst):
    count = 0
    for x in lst:
        if x % 2 == 0:
            count += 1
    return count

lst = list(map(int, input("Enter numbers: ").split()))
print("Even count:", count_evens(lst))
