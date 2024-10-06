class BankAccount:
    def __init__(self,account_balance = 0):
        self.account_balance = account_balance

    def deposit(amount):
        account_balance = account_balance + amount
        return account_balance

    def withdraw(amount):
         if amount <= account_balance:
            account_balance -= amount
            print(f"Withdrew ${amount:.2f}.")
            return True
         else:
             print("Insufficient funds.")
             return False
         
    def display_balance():
        print(f"Current Balance: {self.account_balance}")     