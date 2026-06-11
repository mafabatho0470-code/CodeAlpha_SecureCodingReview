import subprocess
import getpass

def secure_login(username, password):
    # Credentials should come from secure storage, not hardcoded
    stored_username = "codeAlpha"
    stored_password = "Vaseline1212"

    if username == stored_username and password == stored_password:
        print("Login successful!")
    else:
        print("Access denied!")

def run_command():
    cmd = input("Enter a safe command (e.g., dir, whoami): ")
    allowed_commands = ["dir", "echo Hello", "whoami"]
    if cmd in allowed_commands:
        subprocess.run(cmd, shell=True)
    else:
        print("Command not allowed!")

user = input("Username: ")
pwd = getpass.getpass("Password: ")
secure_login(user, pwd)
run_command()
