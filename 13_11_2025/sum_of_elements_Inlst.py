def sum_list(lst):
    total = 0
    for x in lst:
        total += x
    return total

lst = list(map(int, input("Enter numbers: ").split()))
print("Sum:", sum_list(lst))
