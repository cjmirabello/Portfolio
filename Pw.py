import datetime
user_name = input("Please create a user id \n")
password = input("Please create a password \n")
date = datetime.datetime.now()
class bank_account:
    def options(self):
        self.balance = 0
        print("Welcome to your bank account.")
    def deposit(self):
        amount = float(input("How much would you like to deposit \n"))
        self.balance += amount
        print("You deposited ", amount)
    def withdraw(self):
        amount = float(input("How much would you like to withdraw \n"))
        self.balance -= amount
        if self.balance >= 0:
            self.balance -= 0
            print("You withdrew", amount)
        else:
            print("Insufficient funds")
    def net_balance(self):
        print("Your current balance is", self.balance)
x = bank_account()

Username_attempts = 0
while True:
    Username_attempts += 1
    user_name_enter = input("Please enter your username \n")
    if user_name == user_name_enter:

        break
    elif Username_attempts > 2:
        print("Your account has been locked for security purposes")
        quit()
    else:
        print("Please try again")
        continue
password_attempts = 0
while True:
    password_attempts += 1
    password_enter = input("Please enter your password \n")
    if password == password_enter:
        print(date)
        (x.options())
        break
    elif password_attempts > 2:
        print("Your account has been locked for security purposes")
        quit()
    else:
        print("Please try again")
        continue

while True:
    options = input("Type deposit, withdraw, balance, or exit \n")

    if options.lower() == "deposit":
        (x.deposit())
        continue
    if options.lower() == "withdraw":
        (x.withdraw())
        continue
    if options.lower() == "balance":
        (x.net_balance())
        continue
    if options.lower() == "exit":
        print("Thank you.  Have a nice day!")
        quit()
        break
    else:
        print("Please choose a valid option")
        continue