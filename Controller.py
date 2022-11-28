class Account:
    def __init__(self, id="", balance=0):
        self.id = id
        self.balance = balance
        self.pin = '1234'

    def deposit(self, money):
        self.balance += money

    def withdraw(self, money) -> int:
        if self.balance < money:
            return -1
        else:
            self.balance -= money
            return money

    def getbalance(self) -> int:
        return self.balance

    def getpin(self) -> str:
        return self.pin

a = Account()
class ATM:
    def deposit(self, money) -> int:
        a.deposit(money)
        return a.getbalance()
        
    def withdraw(self, money, pin) -> (str, int):
        if a.getpin() == pin:
            if a.withdraw(money) == -1:
                return 'withdraw failed', -1
            else:
                return 'withdraw', a.getbalance()
        else:
            return 'pin not correct', -1
            
    def showBalance(self) -> int:
        return a.getbalance()
