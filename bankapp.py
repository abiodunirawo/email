# Create a method that will add, debit a user and then delete a function: If user account balance is 0,
# User Account name & add method are deleted,thus User Account is deleted. 

import sys

# Create the Class
class Account:
    def _init_(self):
        self.name = 'Grace'
        self.balance = 3000
        self.deposit = 1000
        self.withdrawal = 3000

    def acctname(self):
        return self.name

    def add(self):
        newbal = self.deposit + self.balance
        return newbal

    def debit(self):
        tbalance = self.balance + self.deposit
        newbal2 = tbalance - self.withdrawal
        if self.withdrawal > tbalance:
            print('Your total balance is:',tbalance)
            print('Your withdrawal amount is:',self.withdrawal)
            print('Insufficient funds!')
            sys.exit()

        elif self.withdrawal <= tbalance:
            return newbal2


    def delete(self):
        tbalance = self.balance + self.deposit
        return tbalance


# Create a Child Class of the Parent Class
class Report(Account):
    def result(self):
        print('Account name is:',self.name)
        print('Your initial balance is:',self.balance)
        print('Your deposit is:',self.deposit)
        print('Your total balance is: ',Report.add(self))
        print('Your withdrawal amount is:',self.withdrawal)

        tbalance = (self.balance + self.deposit)
        if tbalance - self.withdrawal == 0:
            print('Your current balance is: ',Report.debit(self))
            del Account.add
            del Account.acctname
            print('Your Account is deleted')
        else:
            print('Your current balance is: ',Report.debit(self))
            print('Your Account is still Active') 


# Create Object of the class
myaccount = Report()
Report.acctname(myaccount)
Report.add(myaccount)
Report.debit(myaccount)
Report.delete(myaccount)

Report.result(myaccount)