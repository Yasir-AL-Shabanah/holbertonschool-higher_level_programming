#!/usr/bin/python3
"""Tiny checkbook application with basic error handling."""

BALANCE_FILE = "balance.txt"


def load_balance():
    """Load current balance from file or start at 0.0."""
    try:
        with open(BALANCE_FILE, "r", encoding="utf-8") as file:
            content = file.read().strip()
            if not content:
                return 0.0
            return float(content)
    except (FileNotFoundError, ValueError):
        return 0.0


def save_balance(balance):
    """Persist balance to file."""
    with open(BALANCE_FILE, "w", encoding="utf-8") as file:
        file.write(f"{balance:.2f}")


def main():
    """Main loop: deposit, withdraw, or quit."""
    balance = load_balance()
    print(f"Current balance: {balance:.2f}")

    while True:
        print("\nChoose an operation:")
        print("  d - deposit")
        print("  w - withdraw")
        print("  q - quit")

        choice = input("> ").strip().lower()

        if choice == "q":
            break

        if choice not in ("d", "w"):
            print("Unknown option.")
            continue

        amount_str = input("Amount: ").strip()
        try:
            amount = float(amount_str)
        except ValueError:
            print("Please enter a numeric amount.")
            continue

        if amount <= 0:
            print("Amount must be positive.")
            continue

        if choice == "d":
            balance += amount
        else:
            if amount > balance:
                print("Insufficient funds, transaction cancelled.")
                continue
            balance -= amount

        print(f"New balance: {balance:.2f}")

    save_balance(balance)
    print("Goodbye!")


if __name__ == "__main__":
    main()
