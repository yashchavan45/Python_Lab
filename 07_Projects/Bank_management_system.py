class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposit Successful")
        print("Current Balance:", self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance!")
        else:
            self.balance -= amount
            print("Withdraw Successful")
            print("Current Balance:", self.balance)

    def check_balance(self):
        print("Available Balance:", self.balance)

    def account_details(self):
        print("===== ACCOUNT DETAILS =====")
        print("Account Holder:", self.name)
        print("Current Balance:", self.balance)


accounts = []


def find_account(name):
    for account in accounts:
        if account.name == name:
            return account
    return None


while True:
    print("\n===== BANK MENU =====")
    print("1. Create Account")
    print("2. Show Accounts")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Check Balance")
    print("6. Account Details")
    print("7. Delete Account")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter account holder name: ")

        found = False

        for account in accounts:
            if account.name == name:
                found = True
                break

        if found:
            print("Account already exists.")
        else:
            start_bal = int(input("Enter starting balance: "))
            user = BankAccount(name, start_bal)
            accounts.append(user)
            print("Account created successfully.")

    elif choice == "2":
        if not accounts:
            print("No accounts found.")
        else:
            print("\n===== ALL ACCOUNTS =====")
            for account in accounts:
                print(account.name, "-", f"₹{account.balance}")

    elif choice == "3":
        name = input("Enter account holder name: ")

        account = find_account(name)

        if account:
            amount = int(input("Enter Deposit Amount: "))
            account.deposit(amount)
        else:
            print("Account not found.")

    elif choice == "4":
        name = input("Enter account holder name: ")
        account = find_account(name)

        if account:
            amount = int(input("Enter withdraw Amount: "))
            account.withdraw(amount)
        else:
            print("Account not found.")

    elif choice == "5":
        name = input("Enter account holder name: ")

        
        account=find_account(name)
        if account:
            account.check_balance()
        else:
            print("Account not found.")

    elif choice == "6":
        name = input("Enter account holder name: ")

        account=find_account(name)
        account.account_details()

    elif choice == "7":
        name = input("Enter account holder name: ")

        account = find_account(name)

        if account:
            accounts.remove(account)
            print("Account deleted successfully.")
        else:
            print("Account not found.")

    elif choice == "8":
        print("Thank you for using our Bank!")
        break

    else:
        print("Invalid Choice!")