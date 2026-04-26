import json
import random
import os

DATA_FILE = "data.json"

# Load users
def load_users():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

# Save users
def save_users(users):
    with open(DATA_FILE, "w") as f:
        json.dump(users, f)

# Register new user
def register():
    users = load_users()

    username = input("Enter username: ")
    if username in users:
        print(" User already exists!")
        return

    pin = str(random.randint(1000, 9999))
    users[username] = {"pin": pin, "balance": 1000}
    save_users(users)

    print(" Account created!")
    print("Your PIN:", pin)

# Generate OTP
def generate_otp():
    return str(random.randint(100000, 999999))

# Login with 3 attempts + OTP
def login():
    users = load_users()

    username = input("Enter username: ")
    if username not in users:
        print(" User not found!")
        return None

    attempts = 3
    while attempts > 0:
        pin = input("Enter PIN: ")

        if pin == users[username]["pin"]:
            otp = generate_otp()
            print(" OTP sent:", otp)   # simulate OTP

            user_otp = input("Enter OTP: ")
            if user_otp == otp:
                print(" Login successful!")
                return username
            else:
                print(" Wrong OTP!")
                return None
        else:
            attempts -= 1
            print(f" Wrong PIN! Attempts left: {attempts}")

    print(" Account locked!")
    return None