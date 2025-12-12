def list_min(lst):
    if not lst: return None
    m = lst[0]
    for x in lst[1:]:
        if x < m: m = x
    return m

def list_max(lst):
    if not lst: return None
    m = lst[0]
    for x in lst[1:]:
        if x > m: m = x
    return m

def list_sum(lst):
    total = 0
    for x in lst:
        total += x
    return total

nums = list(map(int, input("Enter numbers: ").split()))
print("Min:", list_min(nums), "Max:", list_max(nums), "Sum:", list_sum(nums))
