class BankAccount:
    def __init__(self, initial_balance=0):
        self._account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount
            print(f"Deposited: ${amount:.1f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self._account_balance >= amount:
                self._account_balance -= amount
                print(f"Withdrew: ${amount:.1f}")
                return True
            else:
                print(f"Insufficient funds to withdraw ${amount:.1f}.")
                return False
        else:
            print("Withdrawal amount must be positive.")
            return False

    def display_balance(self):
        print(f"Current Balance: ${self._account_balance:.1f}")

