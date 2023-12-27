# mybank.py

class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"${amount} deposited. Current balance: ${self.balance}"
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"${amount} withdrawn. Current balance: ${self.balance}"
        else:
            return "Invalid withdrawal amount or insufficient funds."

    def get_balance(self):
        return f"Current balance for {self.account_holder}: ${self.balance}"


if __name__ == "__main__":
    # Example usage
    account1 = BankAccount("John Doe", 1000)
    print(account1.get_balance())
    print(account1.deposit(500))
    print(account1.withdraw(200))
    print(account1.get_balance())
