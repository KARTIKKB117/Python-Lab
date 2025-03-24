def is_palindrome_number(n):
    return str(n) == str(n)[::-1]  # Convert number to string and check

num = int(input("Enter a number: "))

print("Palindrome!" if is_palindrome_number(num) else "Not a palindrome.")
