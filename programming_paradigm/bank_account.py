

class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initializes the account with a starting balance (default is 0).
        """
        self.account_balance = initial_balance

    def deposit(self, amount):
        """
        Adds money to the account.
        """
        self.account_balance += amount

    def withdraw(self, amount):
        """
        Withdraws money from the account if there are sufficient funds.
        Returns True if successful, False otherwise.
        """
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """
        Prints the current balance in a user-friendly way.
        """
        print(f"Current Balance: ${self.account_balance}")
