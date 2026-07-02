'''===== BANK MENU =====

1. Deposit
2. Withdraw
3. Check Balance
4. Exit'''

class Bankacc:
    def __init__(self, name, balance):  
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposit successful")
        print("Current balance:", self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print("Withdraw successful")
            print("Current balance:", self.balance)

    def check_balance(self):
        print("Available Balance:", self.balance)


ac_name = input("Enter account holder name: ")
user1 = Bankacc(ac_name, 0)

while True:
    print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")
    n = input("Enter your choice: ")

    if n == "1":
        d = int(input("Enter deposit amount: "))
        user1.deposit(d)
    elif n == "2":
        w = int(input("Enter withdraw amount: "))
        user1.withdraw(w)
    elif n == "3":
        user1.check_balance()
    elif n == "4":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")