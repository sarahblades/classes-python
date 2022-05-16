nextNumber = 100000

class BankAccount:
    def __init__(self, name: str, accountNum: int = None, balance: float = 0) -> None:
        self._name = name

        if accountNum is None:
            accountNum = self.getNext()
        self._accountNum = accountNum

        self._balance = balance

    def getNext(self):
        global nextNumber
        next = nextNumber
        nextNumber += 1
        return next

    def deposit(self, amount: float) -> bool:
        if amount <= 0:
             print("Amount to deposit must be greater than zero.")

        self._balance += amount
        print(f"{amount} has been deposited. New balance is {self._balance}")
        return True

    def withdraw(self, amount: float) -> bool:
        if amount <= 0:
            print("Amount to withdraw must be greater than zero.")
        if amount > self._balance:
            print("Amount to withdraw is greater than balance.")

        self._balance -= amount

        print(f"{amount} has been withdrawn. New balance is {self._balance}")
        return True

    def getDetails(self) -> None:
        print(f"Account name = {self._name}")
        print(f"Account number = {self._accountNum}")
        print(f"Current balance = {self._balance}")


class CurrentAccount(BankAccount):
    def __init__(self, overdraftLimit: float, name: str, accountNum: int = None, balance = 0) -> None:
        super().__init__(name, accountNum, balance)
        self._overdraftLimit = overdraftLimit

    def withdraw(self, amount: float) -> bool:
        if abs(self._balance - amount) > self._overdraftLimit:
            print("Withdrawing that amount will take you over your overdraft limit")
        else:
            if amount <= 0:
                print("Amount to withdraw must be greater than zero.")

            self._balance -= amount

            print(f"{amount} has been withdrawn. New balance is {self._balance}")
            return True

    def getDetails(self) -> None:
        super(CurrentAccount, self).getDetails()
        print(f"Overdraft limit = {self._overdraftLimit}")


class SavingsAccount(BankAccount):
    def __init__(self, interestRate: float, name: str, accountNum: int = None, balance: float = 0) -> None:
        super().__init__(name, accountNum, balance)
        self._interestRate = interestRate

    def addInterest(self) -> bool:
        self._balance += (self._interestRate * self._balance)
        print(f"Interest added. New balance is {self._balance}")
        return True

    def getDetails(self) -> None:
        super(SavingsAccount, self).getDetails()
        print(f"Interest rate = {self._interestRate}")
