class Customer:
    def _init_(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone
        self.accounts = []
    def add_account(self, account):
        self.accounts.append(account)
    def remove_account(self, account):
        self.accounts.remove(account)
class Account:
    def _init_ (self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds!")

    def display_balance(self):
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance}")

c1 = Customer("John Doe", "Jaipur","12345689")
account1 = Account("123456789", 1000)
account2 = Account("987654321", 500)
c1.add_account(account1)
c1.add_account(account2)
account1.deposit(500)
account2.withdraw(200)
account1.display_balance()
account2.display_balance()
