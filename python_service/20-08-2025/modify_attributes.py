class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def show_balance(self):
        print(f"Balance: ${self.balance}")

acc = BankAccount(100)
acc.deposit(50)
acc.show_balance()