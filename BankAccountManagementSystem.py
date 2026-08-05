##  Bank Account Management System

class Account:
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    # Deposit Money
    def deposit(self, amount):
        self.balance += amount
        print("Amount Deposited Successfully")


    # Withdraw Money 
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdraw Successfully")
        else:
            print("Insufficient Balance")

    # Balance check
    def check_balance(self):
        print(f"balance Amount is Rs. {self.balance}")


    # Display account details
    def display(self):
        print("\n------ Account Details ------")
        print("account No : ", self.acc_no)
        print("Name : ", self.name)
        print("Balance : ", self.balance)
        print("------------------------------")

class AccountManagementSystem:
    def __init__(self):
        self.account = []

    # Find Account
    def find_account(self, acc_no):
        for account in self.account:
            if account.acc_no == acc_no:
                return account
            return None

    # Create Account
    def Create_Account(self):
        acc_no = int(input("Enetr Account Number: "))
        name = input("Enter Account Holder Name: ")
        balance = float(input("Enter Balance: "))

        account = Account(acc_no, name, balance)
        self.account.append(account)

        print("Account Created Successfully")

    # Deposit money
    def deposit_money(self):
        acc_no = int(input("Enter account No: "))
        account = self.find_account(acc_no)

        if account:
            amount = float(input("Enter Deposit Amount: "))
            account.deposit(amount)


        else:
            print("Account Not Found!")


    # Withdraw Money
    def withdraw_money(self):
        acc_no = int(input("Enter Account No: "))
        account = self.find_account(acc_no)

        if account:
            amount = float(input("Enter withdraw Amount: "))
            account.withdraw(amount)

    # Check Balance
    def check_balance(self):
        acc_no = int(input("Enter Account No "))
        account = self.find_account(acc_no)
        

        if account:
            account.check_display()
        else:
            print("Account Not Found")
            
    # View Account Details
    def view_account(self):
        acc_no = int(input("Enter account Number: "))
        account = self.find_account(account)

        if account:
            account.display()
        else:
            print("Account Not Found")


    # Display All Accounts
    def display_All(self):
        if not self.account:
            print("No Accounts Found")
            return

        for account in self.account:
            account.display()



system = AccountManagementSystem()

while True:

        print("\n===== Account Management System =====")
        print("1. Create Account")
        print("2. Deposit Amount")
        print("3. withdraw Amount")
        print("4. Check Balance")
        print("5. View Account Details")
        print("6. Display All Accounts")
        print("7. Exit")

        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            system.Create_Account()
        elif choice == 2:
            system.deposit_money()
        elif choice == 3:
            system.withdraw_money()
        elif choice == 4:
            system.check_balance()
        elif choice == 5:
            system.view_account()
        elif choice == 6:
            system.display_All()
        elif choice == 7:
            print("Systwm Closed!")
            break
        else:
            print("Invalid Choice!")
            


            

            






        


