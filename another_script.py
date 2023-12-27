# another_script.py

from mybank import BankAccount

# Create a new bank account
account2 = BankAccount("Jane Doe", 1500)

# Use the methods of the BankAccount class
print(account2.get_balance())
print(account2.deposit(200))
print(account2.withdraw(300))
print(account2.get_balance())
