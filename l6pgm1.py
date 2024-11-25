class BankAccount:
    def __init__(self, name, account_number, account_type, balance=0):
        self.name = name
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}")

    def display_details(self):
        print("\nAccount Details:")
        print(f"Name: {self.name}")
        print(f"Account Number: {self.account_number}")
        print(f"Account Type: {self.account_type}")
        print(f"Balance: {self.balance}")

def main():
    name = input("Enter account holder's name: ")
    account_number = input("Enter account number: ")
    account_type = input("Enter account type (e.g., Savings, Checking): ")
    initial_balance = float(input("Enter initial balance (default is 0): "))

    account = BankAccount(name, account_number, account_type, initial_balance)
    account.display_details()

    while True:
        print("\nSelect an option:")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Display Account Details")
        print("4. Exit")

        option = input("Enter your choice (1-4): ")

        if option == '1':
            deposit_amount = float(input("Enter the amount to deposit: "))
            account.deposit(deposit_amount)
        elif option == '2':
            withdraw_amount = float(input("Enter the amount to withdraw: "))
            account.withdraw(withdraw_amount)
        elif option == '3':
            account.display_details()
        elif option == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()

