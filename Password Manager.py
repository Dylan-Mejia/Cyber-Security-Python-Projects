import hashlib
import getpass

print("Welcome to Password Manager!")
password_manager = {}

def create_account():
    print("Create an Account")
    username = input("Create a username: ")
    password = getpass.getpass("Create a password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    password_manager[username] = hashed_password
    print("Account successfully created!")

def login():
    print("Login")
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if username in password_manager.keys() and password_manager[username] == hashed_password:
        print("Login Successful!")
    else:
        print("Invaid username or password!")

def main():
    while True:
        choice = input("Enter 1 to create an account, 2 to login, 3 to display usernames, or 0 to exit: ")
        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "3":
            print(password_manager)
        elif choice == "0":
            break
        else:
            print("Invalid Choice!")

if __name__ == "__main__":
    main()
