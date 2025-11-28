# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0.0):
        # initialize balance (default to 0 if not provided)
        self._balance = float(initial_balance)

    def deposit(self, amount):
        """Deposit amount into account balance."""
        if amount < 0:
            raise ValueError("Cannot deposit a negative amount.")
        self._balance += amount

    def withdraw(self, amount):
        """Withdraw amount if sufficient funds exist. Return True if success, else False."""
        if amount < 0:
            raise ValueError("Cannot withdraw a negative amount.")
        if amount <= self._balance:
            self._balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Print the current balance in a user-friendly format."""
        print(f"Current Balance: ${self._balance:.2f}")
