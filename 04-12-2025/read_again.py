filename = "Muneer.txt"
with open(filename, "r", encoding="utf-8") as file:
    print("Updated file content:")
    print(file.read())
