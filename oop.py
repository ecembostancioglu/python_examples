class Account:
    def __init__(self,name,number,balance):
        self.name = name
        self.number = number
        self.balance = balance
    def accountInfo(self):
        print("Name:",self.name)
        print("Number:",self.number)
        print("Balance:",self.balance)
    def withdrawself(self,amount):
        if (self.balance - amount < 0 ):
            print("You have insufficient balance")
        else:
            self.balance -= amount
            print("New balance:",self.balance)
    def deposit(self,amount):
        self.balance += amount
        print("New balance:",self.balance)


account=Account("Ecem B",123456,1000)    
account.accountInfo()   #Name: Ecem B Number: 123456 Balance: 1000 


account.withdrawself(800)

account.deposit(500)