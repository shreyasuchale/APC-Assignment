class BankAccount:
    account_counter = 1000

    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0
        BankAccount.account_counter += 1
        self.account_number = BankAccount.account_counter

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    def display_balance(self):
        print("Account Holder:", self.account_holder)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)

    def transfer(self, amount, other_account):
        if self.balance >= amount:
            self.balance -= amount
            other_account.balance += amount
            print("Transferred:", amount)
        else:
            print("Insufficient balance for transfer")


account1 = BankAccount("Shreyas Uchale")
account2 = BankAccount("shreyash Kumbhar")

account1.deposit(5000)
account1.withdraw(1000)
account1.transfer(2000, account2)

account1.display_balance()
account2.display_balance()