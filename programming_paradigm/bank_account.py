

class BankAccount:
    def __init__(self, amount):
        self.account_balance = amount
        
    
    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
        else:
            print("You can't deposite an amount less than 0.")
             
    def withdraw(self, amount):
        if self.account_balance >= amount:
            return True
        else:
            return False
        
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}")