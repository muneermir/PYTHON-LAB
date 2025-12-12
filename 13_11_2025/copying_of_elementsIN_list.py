def copy_list(src):
    dest = []
    for x in src:
        dest.append(x)
    return dest

src = input("Enter items: ").split()
dest = copy_list(src)
print("Copied list:", dest)
