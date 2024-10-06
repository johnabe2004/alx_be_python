class BankAccount:
    def __init__(self, initial_balance=0):
        self._account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self._account_balance >= amount:
                self._account_balance -= amount
                print(f"Withdrew: ${amount:.2f}")
                return True
            else:
                print(f"Insufficient funds to withdraw ${amount:.2f}.")
                return False
        else:
            print("Withdrawal amount must be positive.")
            return False

    def display_balance(self):
        """Display the current balance."""
        print(f"Current Balance: ${self._account_balance:.2f}")

