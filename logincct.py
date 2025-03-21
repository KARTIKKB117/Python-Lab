stored_username = "user"
stored_password = "pass123"

username = input("Enter username: ")
password = input("Enter password: ")

if username == stored_username and password == stored_password:
    print("Login successful!")
else:
    print("Invalid credentials!")
