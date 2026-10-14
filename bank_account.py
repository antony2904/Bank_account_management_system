class BankAccount:
    def __init__(self, account_holder_name: str, account_number: str, initial_balance: float = 0.0):
        self.account_holder_name = account_holder_name.strip()
        self.account_number = account_number
        self.balance = float(initial_balance)

    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount:,.2f}")
            return True
        print("Error: Deposit amount must be positive.")
        return False

    def withdraw(self, amount: float):
        if amount <= 0:
            print("Error: Withdrawal amount must be positive.")
            return False
        if amount > self.balance:
            print("Error: Insufficient balance.")
            return False
        self.balance -= amount
        print(f"Withdrawn: ${amount:,.2f}")
        return True

    def display_balance(self):
        print(f"Current Balance: ${self.balance:,.2f}")

    def display_details(self):
        print("\n--- Account Details ---")
        print(f"Account Holder: {self.account_holder_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance       : ${self.balance:,.2f}")


def run_menu(account: BankAccount):
    while True:
        print("\n--- BANK MENU ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Account Details")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            try:
                amt = float(input("Enter amount to deposit: "))
                account.deposit(amt)
            except ValueError:
                print("Error: Invalid number format.")

        elif choice == "2":
            try:
                amt = float(input("Enter amount to withdraw: "))
                account.withdraw(amt)
            except ValueError:
                print("Error: Invalid number format.")

        elif choice == "3":
            account.display_balance()

        elif choice == "4":
            account.display_details()

        elif choice == "5":
            print("Thank you for using our service.")
            break

        else:
            print("Invalid choice. Please select 1 through 5.")


if __name__ == "__main__":
    accounts = [
        BankAccount("Jane", "ACC1001", 51000.0),
        BankAccount("Alan", "ACC1002", 53000.0),
        BankAccount("John", "ACC1003", 56600.0),
        BankAccount("Anna", "ACC1004", 189000.0),
        BankAccount("Mary", "ACC1005", 150500.0),
        BankAccount("Vincent", "ACC1006", 256000.0),
    ]

    user_name = input("Enter account holder name: ").strip()

    matched_account = None
    for acc in accounts:
        if acc.account_holder_name.casefold() == user_name.casefold():
            matched_account = acc
            break

    if matched_account:
        run_menu(matched_account)
    else:
        print(f"No account found under the name '{user_name}'.")