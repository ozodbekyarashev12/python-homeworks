import json


class Account:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"{amount} deposited. New balance: {self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance."
        self.balance -= amount
        return f"{amount} withdrawn. New balance: {self.balance}"


class Bank:
    def __init__(self):
        self.accounts = {}
        self.load_from_file()

    def create_account(self, name, initial_deposit):
        account_number = len(self.accounts) + 1
        new_account = Account(account_number, name, initial_deposit)
        self.accounts[account_number] = new_account
        self.save_to_file()
        return f"Account created for {name}. Account Number: {account_number}"

    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            return f"Account Number: {account.account_number}, Name: {account.name}, Balance: {account.balance}"
        return "Account not found."

    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            return account.deposit(amount)
        return "Account not found."

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            return account.withdraw(amount)
        return "Account not found."

    def save_to_file(self):
        with open("accounts.json", "w") as file:
            json.dump({acc: vars(self.accounts[acc]) for acc in self.accounts}, file)

    def load_from_file(self):
        try:
            with open("accounts.json", "r") as file:
                accounts_data = json.load(file)
                for acc_num, acc_data in accounts_data.items():
                    self.accounts[int(acc_num)] = Account(**acc_data)
        except FileNotFoundError:
            pass


# Example Usage
bank = Bank()

print(bank.create_account("Alice", 1000))
print(bank.deposit(1, 500))
print(bank.withdraw(1, 200))
print(bank.view_account(1))