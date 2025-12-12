def set_add(s, elem):
    s.add(elem)

def set_remove(s, elem):
    s.discard(elem)  # discard won't raise if missing

def set_search(s, elem):
    return elem in s

def set_union(a, b):
    return a.union(b)

def set_intersection(a, b):
    return a.intersection(b)

# Example
A = {1,2,3}
B = {3,4,5}
set_add(A, 6)
set_remove(B, 5)
print("Search 2 in A:", set_search(A, 2))
print("Union:", set_union(A, B))
print("Intersection:", set_intersection(A, B))
