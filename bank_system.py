
class BankAccount:
    
    def __init__(self, account_holder: str, initial_balance: float = 0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def __str__(self):
        return f"Bank account holder: {self.account_holder}, Account balance: {self.balance}"

    def deposit(self, depositAmount:float):
        self.balance += depositAmount
        return f"Account balance updated successfully. current balance: {self.balance}"
    
    def withdraw(self, withdrawAmount: float):
        if withdrawAmount > self.balance:
            raise Exception ("Insufficient funds!")
        self.balance -= withdrawAmount
        return f"Account balance updated successfully. current balance: {self.balance}"

    def get_balance(self):
        return f"Account balance: {self.balance}"
    
    def get_account_holder(self):
        return f"Account holder: {self.account_holder}"