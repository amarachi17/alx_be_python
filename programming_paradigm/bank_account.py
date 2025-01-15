class BankAccount:
    def __init__(self, initial_balance=0):
        # Initialize the bank account with an optional initial
        self.__account_balance = initial_balance
        
    def deposit(self, amount):
        # Add the specified amount to the account balance
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposited amount must be greater than zero")
        
    def withdraw(self, amount):
        # Deducting the amount from the account
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False
        
    def display_balance(self):
        # Printing the current account balance
        print(f"Current Balance: ${self.__account_balance: .2f}")