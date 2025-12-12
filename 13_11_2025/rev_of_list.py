def reverse_list(lst):
    rev = []
    for i in range(len(lst)-1, -1, -1):
        rev.append(lst[i])
    return rev

lst = input("Enter items separated by space: ").split()
print("Reversed:", reverse_list(lst))
