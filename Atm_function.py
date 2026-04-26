import json
from datetime import datetime

DATA_FILE = "data.json"
TRANS_FILE = "transactions.txt"

def load_users():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(DATA_FILE, "w") as f:
        json.dump(users, f)

# Save transaction
def log_transaction(username, action, amount):
    with open(TRANS_FILE, "a") as f:
        f.write(f"{datetime.now()} | {username} | {action} | {amount}\n")

def check_balance(username):
    users = load_users()
    print("💰 Balance:", users[username]["balance"])

def deposit(username):
    users = load_users()
    amount = int(input("Enter amount: "))

    users[username]["balance"] += amount
    save_users(users)
    log_transaction(username, "DEPOSIT", amount)

    print("✅ Deposited!")

def withdraw(username):
    users = load_users()
    amount = int(input("Enter amount: "))

    if amount > users[username]["balance"]:
        print("❌ Insufficient balance!")
    else:
        users[username]["balance"] -= amount
        save_users(users)
        log_transaction(username, "WITHDRAW", amount)

        print("✅ Withdrawn!")

def show_transactions():
    try:
        with open(TRANS_FILE, "r") as f:
            print("\n📜 Transaction History:")
            print(f.read())
    except:
        print("No transactions yet.")