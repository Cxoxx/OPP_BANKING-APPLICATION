################################
#  NAME: Chimi Dorji
#  DEPARTMENT: EE
#  INDEX NO: 02230059
################################
# REFERENCES
# Slatkin, B. (2019). Effective Python: 90 Specific Ways to Write Better Python. United Kingdom: Pearson Education, Limited.
# O'Reilly, D. (2021). Python Programming: This Book Includes: Python for Beginners - Python for Data Science. (n.p.): Daniele Pecile.
################################


import random

class BankAccount:
    def __init__(self, account_number, balance, account_type):
        self.account_number = account_number  # Decide on the account number
        self.balance = balance  # mention your account number
        self.account_type = account_type  # Determine the type of account

    def deposit(self, amount):
        self.balance += amount  #The deposited money is added to the balance.
        return self.balance  # Given the new balance.

    def withdraw(self, amount):
        if amount <= self.balance:  # Determine whether the withdrawal amount is equal to or less than the balance.
            self.balance -= amount  # Remove the money from your balance.
            return self.balance  # Given the new balance
        else:
            return "Insufficient funds"  # If the withdrawal amount exceeds the balance, a return message is displayed.

class PersonalAccount(BankAccount):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance, "Personal")  # created for the personal account type.

class BusinessAccount(BankAccount):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance, "Business")  # created for the business account type.

class Bank:
    def __init__(self):
        self.accounts = {}  # To save accounts, an empty dictionary is established.

    def create_account(self, account_type):
        account_number = random.randint(10000, 99999)  # Account numbers are generated at random.
        balance = 0  # the balance to zero.
        if account_type.lower() == "personal":
            account = PersonalAccount(account_number, balance)  # Create something for your own account.
        elif account_type.lower() == "business":
            account = BusinessAccount(account_number, balance)  # create something for businesss account.
        else:
            return "Invalid account type"  # The message returned is for an invalid account type.
        
        with open("accounts.txt", "a") as file:
            file.write(f"{account_number},{account_type},{balance}\n")  # Include account details in the file.
        
        self.accounts[account_number] = account  # Add account information to the dictionary.
        return account_number  # Number assigned to the account in response

    def login(self, account_number):
        with open("accounts.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                if int(data[0]) == account_number:
                    account_type = data[1]
                    balance = float(data[2])
                    if account_type == "Personal":
                        return PersonalAccount(account_number, balance)  # Replug in the personal account object again.
                    elif account_type == "Business":
                        return BusinessAccount(account_number, balance)  #Replug in the business account object again.
                    else:
                        return None  # If you don't know what type of account it is, return None.


    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            return self.accounts[account_number].deposit(amount)  # The amount placed in the account
        else:
            return "Account not found"  # If there is no account, a notice is displayed.
    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            return self.accounts[account_number].withdraw(amount)  # Withdraw money from the account
            
        else:
            return "Account not found"  # If there is no account, a notice is displayed.
    def delete_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]  # Eliminate the account from the lexicon.
            with open("accounts.txt", "r") as file:
                lines = file.readlines()  # Remove the account from the vocabulary.
            with open("accounts.txt", "w") as file:
                for line in lines:
                    if line.split(",")[0] != str(account_number):
                        file.write(line)  # change the file without erasing the deleted account
            return "Account deleted"  # Message was returned after successful deletion.
        else:
            return "Account not found"  # If the account cannot be found, a notice is displayed.


def main():
    bank = Bank()  # Construct a banking entity.
    while True:
        print("\n1. Open Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            account_type = input("Enter account type (Personal/Business): ")
            account_number = bank.create_account(account_type)  # Start a new account.
            print(f"Account created successfully with number: {account_number}")
        elif choice == "2":
            account_number = int(input("Enter account number: "))
            account = bank.login(account_number)  # Log into your current account.
            if account:
                while True:
                    print("\n1. Deposit")
                    print("2. Withdraw")
                    print("3. Delete Account")
                    print("4. Logout")
                    operation = input("Enter operation choice: ")
                    if operation == "1":
                        amount = float(input("Enter deposit amount: "))
                        print(f"New balance: {bank.deposit(account_number, amount)}")
                    elif operation == "2":
                        amount = float(input("Enter withdrawal amount: "))
                        print(f"New balance: {bank.withdraw(account_number, amount)}")
                    elif operation == "3":
                        print(bank.delete_account(account_number))  # Remove the account.
                        break
                    elif operation == "4":
                        break
                    else:
                        print("Invalid operation choice.")
            else:
                print("Invalid account number.")
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()