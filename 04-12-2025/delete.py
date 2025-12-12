import os
filename = "Muneer.txt"
if os.path.exists(filename):
    os.remove(filename)
    print("File deleted successfully.")
else:
    print("File not found.")
