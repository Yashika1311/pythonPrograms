# account_manager.py

from mybank import BankAccount

class AccountManager:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def get_all_balances(self):
        return [account.get_balance() for account in self.accounts]







