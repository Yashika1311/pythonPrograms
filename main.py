# main.py

from mybank import BankAccount
from account_manager import AccountManager

if __name__ == "__main__":
    # Example usage

    # Create bank accounts
    account1 = BankAccount("John Doe", 1000)
    account2 = BankAccount("Jane Doe", 1500)

    # Create an account manager
    manager = AccountManager()

    # Add accounts to the manager
    manager.add_account(account1)
    manager.add_account(account2)

    # Perform operations
    print("Balances before transactions:")
    print(manager.get_all_balances())

    print(account1.deposit(500))
    print(account2.withdraw(200))

    print("Balances after transactions:")
    print(manager.get_all_balances())
