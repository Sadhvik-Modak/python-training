class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Private attribute
        self.__balance = balance                # Private attribute

    # Public method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive")

    # Public method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdrawal amount")

    # Public method to get the current balance
    def get_balance(self):
        return self.__balance

# Create an object of the BankAccount class
account = BankAccount("123456789", 1000)

# Deposit money into the account
account.deposit(500)
print(account.get_balance())  # Output: 1500

# Withdraw money from the account
account.withdraw(200)
print(account.get_balance())  # Output: 1300

# Attempting to withdraw an invalid amount
account.withdraw(2000)        # Output: Invalid withdrawal amount
print(account.get_balance())  # Output: 1300