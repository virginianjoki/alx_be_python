class BankAccount:
    def __init__(self,account_balance = 0.0):
        self.account_balance = account_balance

    def deposit(self,amount):
        self.account_balance = self.account_balance + amount

    def withdraw(self, amount):
        """Withdraw the amount if funds are sufficient."""
        if self.account_balance >= amount:
            self.account_balance -= amount  # Correct this line to modify account_balance
            print(f"Withdrew: ${amount}")
            return True
        else:
            print(f"Insufficient funds to withdraw ${amount}.")
            return False    

         
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")     