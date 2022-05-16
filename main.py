from accounts import BankAccount, CurrentAccount, SavingsAccount

accountb = BankAccount(name="Sarah Blades", balance=50000)
accountb.deposit(4000)
accountb.getDetails()

accountb2 = BankAccount(name= "Justin Foster")
print("\n")
accountb2.getDetails()

accountc = CurrentAccount(name="Jane Blades", overdraftLimit=500)
print("\n")
accountc.getDetails()
accountc.withdraw(600)
accountc.withdraw(300)
print("\n")
accountc.getDetails()