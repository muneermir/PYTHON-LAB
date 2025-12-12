def largest_in_list(lst):
    if not lst:
        return None
    max_val = lst[0]
    for x in lst[1:]:
        if x > max_val:
            max_val = x
    return max_val

lst = list(map(int, input("Enter numbers separated by space: ").split()))
print("Largest:", largest_in_list(lst))
