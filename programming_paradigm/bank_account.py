class BankAccount:
    def __init__(self,account_balance = 0.0):
        self.account_balance = account_balance

    def deposit(self,amount):
        self.account_balance = self.account_balance + amount

    def withdraw(self,amount):
         if 0 < amount <= self.account_balance:
            self.account_balance = self.amount -amount
            return True
         else:
             print("Insufficient funds.")
             return False
         
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")     