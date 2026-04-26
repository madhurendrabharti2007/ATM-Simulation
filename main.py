import user_verification as auth
import Atm_function as atm

def atm_menu(username):
    while True:
        print("\n----- ATM MENU -----")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transaction History")
        print("5. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            atm.check_balance(username)
        elif choice == "2":
            atm.deposit(username)
        elif choice == "3":
            atm.withdraw(username)
        elif choice == "4":
            atm.show_transactions()
        elif choice == "5":
            print(" Logged out!")
            break
        else:
            print(" Invalid choice!")

def main():
    while True:
        print("\n===== ATM SYSTEM =====")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            auth.register()
        elif choice == "2":
            user = auth.login()
            if user:
                atm_menu(user)
        elif choice == "3":
            print(" Thank you!")
            break
        else:
            print(" Invalid choice!")

main()