# Deliberately Vulnerable Login System
# For Security Review Purposes Only

users = {
    "admin": "admin123",
    "user": "password123"
}

while True:

    username = input("Username: ")
    password = input("Password: ")

    # Vulnerability 1: Username Enumeration
    if username not in users:
        print("Username does not exist.")
        continue

    # Vulnerability 2: Plain Text Passwords
    if users[username] == password:

        # Vulnerability 3: Sensitive Information Disclosure
        print("Login Successful")
        print(f"Welcome {username}")
        print(f"Your password is: {password}")

        # Vulnerability 4: Excessive Privileges
        if username == "admin":
            print("Admin Access Granted")

        break

    else:
        print("Incorrect password")

    # Vulnerability 5: No Account Lockout
    # Unlimited login attempts
