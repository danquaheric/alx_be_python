# main-0.py

import sys
from bank_account import BankAccount

def main():
    # You can change the initial balance here as needed
    account = BankAccount(100.0)  # Example starting balance of $100

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Expect first argument like "deposit:50" or "withdraw:20" or "display"
    arg = sys.argv[1]
    parts = arg.split(':')
    command = parts[0].lower()

    amount = None
    if len(parts) > 1 and parts[1] != "":
        try:
            amount = float(parts[1])
        except ValueError:
            print("Amount must be a number.")
            sys.exit(1)

    if command == "deposit" and amount is not None:
        try:
            account.deposit(amount)
            print(f"Deposited: ${amount}")
        except ValueError as ve:
            print(f"Error: {ve}")
    elif command == "withdraw" and amount is not None:
        try:
            success = account.withdraw(amount)
            if success:
                print(f"Withdrew: ${amount}")
            else:
                print("Insufficient funds.")
        except ValueError as ve:
            print(f"Error: {ve}")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command or missing amount.")

if __name__ == "__main__":
    main()
