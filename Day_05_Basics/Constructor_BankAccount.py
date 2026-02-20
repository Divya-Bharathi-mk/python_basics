class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder=account_holder
        self.balance=balance
        
    def display(self):
        print("Account holder: ", self.account_holder)
        print("Current Balance: ", self.balance )
        
    def deposit(self, amount):
        self.balance=self.balance+amount
        return self.balance
        
    def withdraw(self, amount):
        if amount<=0:
            print("Enter amount should not be negative or 0")
            return None
        elif amount>self.balance:
            print("Insufficient balance")
            return None
        else:
            self.balance =self.balance-amount
            return self.balance,amount
        
    def display_balance(self):
        return self.balance
    
obj1=BankAccount("Divya")
obj1.display()
deposit=obj1.deposit(1000)
print("The with deposit account balance: ",deposit)

result=obj1.withdraw(300)
if result is not None:
       withdraw,amount=result
       print("After withdraw amount is ",withdraw,"account balance is: ",amount)

        
    
        
