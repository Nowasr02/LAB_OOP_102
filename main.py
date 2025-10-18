from bank_system import BankAccount


account1 = BankAccount("Norah", 700)
account2 = BankAccount("Waleed", 1500)
account3 = BankAccount("Yasmeen")


print(account1)
print(account2)
print(account3)


print(account1.deposit(300))
print(account2.withdraw(450))
print(account2.get_account_holder())
print(account1.get_balance())