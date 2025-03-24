import re

def is_palindrome(s):
    s = re.sub(r'[^a-zA-Z0-9]', '', s.lower())  # Remove non-alphanumeric characters
    return s == s[::-1]

phrase = input("Enter a phrase: ")

print("Palindrome!" if is_palindrome(phrase) else "Not a palindrome.")
