# Create a bank account class that has attributes owner, balance and two methods deposit and withdraw. 
# Withdrawals may not exceed the available balance. Instantiate your class, make several deposits and withdrawals, 
# and test to make sure the account can't be overdrawn.


class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        self.balance -= amount
        print(f"Withdrawn ${amount}. New balance: ${self.balance}")

owner_full_name = input("Enter the full name of owner: ")  
bb = int(input("Enter the initial balance: "))

account = Account(owner_full_name, bb)

account.deposit(100)
account.deposit(50)

account.withdraw(30)
account.withdraw(200)
