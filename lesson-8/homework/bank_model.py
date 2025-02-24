import json
class Account:
    def __init__(self, account_number, name, initial_deposit):
        self.account_number = account_number
        self.name = name
        self.balance = initial_deposit

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def __str__(self):
        return f"Account Number: {self.account_number}, Name: {self.name}, Balance: {self.balance}"



class Bank:
    def __init__(self):
        self.accounts = {}
        self.load_from_file()

    def create_account(self, name, initial_deposit):
        account_number = len(self.accounts) + 1
        new_account = Account(account_number, name, initial_deposit)
        self.accounts[account_number] = new_account
        self.save_to_file()
        return account_number

    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            return str(account)
        return "Account not found."

    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account and account.deposit(amount):
            self.save_to_file()
            return "Deposit successful."
        return "Deposit failed."

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account and account.withdraw(amount):
            self.save_to_file()
            return "Withdrawal successful."
        return "Withdrawal failed."

    def save_to_file(self):
        with open('accounts.txt', 'w') as file:
            accounts_data = {acc_num: acc.__dict__ for acc_num, acc in self.accounts.items()}
            json.dump(accounts_data, file)

    def load_from_file(self):
        try:
            with open('accounts.txt', 'r') as file:
                accounts_data = json.load(file)
                for acc_num, acc_data in accounts_data.items():
                    self.accounts[int(acc_num)] = Account(**acc_data)
        except FileNotFoundError:
            pass

bank = Bank()

while True:
    print("\nBank Menu:")
    print("1. Create Account")
    print("2. View Account")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter your name: ")
        initial_deposit = float(input("Enter initial deposit: "))
        account_number = bank.create_account(name, initial_deposit)
        print(f"Account created successfully. Your account number is {account_number}.")

    elif choice == '2':
        account_number = int(input("Enter your account number: "))
        print(bank.view_account(account_number))

    elif choice == '3':
        account_number = int(input("Enter your account number: "))
        amount = float(input("Enter amount to deposit: "))
        print(bank.deposit(account_number, amount))

    elif choice == '4':
        account_number = int(input("Enter your account number: "))
        amount = float(input("Enter amount to withdraw: "))
        print(bank.withdraw(account_number, amount))

    elif choice == '5':
        break

    else:
        print("Invalid choice. Please try again.")