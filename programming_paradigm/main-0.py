import sys
from bank_account import BankAccount


def main():
    # Initialize a bank account with optional balance from command line arguments
    if len(sys.argv) > 1:
        try:
            initial_balance = float(sys.argv[1])
        except ValueError:
            print("Invalid initial balance. Please enter a valid number.")
            return
    else:
        initial_balance = 0

    account = BankAccount(initial_balance)
    print(f"Bank account created with initial balance of ${initial_balance:.2f}")

    # Main command loop
    while True:
        print("\nOptions: deposit, withdraw, balance, exit")
        user_input = input("Enter a command: ").lower()

        if user_input == "deposit":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)

        elif user_input == "withdraw":
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)

        elif user_input == "balance":
            account.display_balance()

        elif user_input == "exit":
            print("Exiting the program.")
            break

        else:
            print("Invalid command. Please choose one of the available options.")


if __name__ == "__main__":
    main()

