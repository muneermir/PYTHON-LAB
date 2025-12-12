def is_palindrome_number(n):
    s = str(n)
    return s == s[::-1]

num = int(input("Enter number: "))
print("Palindrome" if is_palindrome_number(num) else "Not palindrome")
