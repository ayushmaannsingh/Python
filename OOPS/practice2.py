# Create Account class with 2 attributes - balance and account no.
# Create methods for debit, credit and printing the balance.

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
            self.balance -= amount
            print("Rs.", amount, "was debited")
            print("total balance = ", self.get_balance())
        
    def credit(self, amount):
            self.balance += amount
            print("Rs.", amount, "was credited")
            print("total balance =", self.get_balance())

    def get_balance(self):
            return self.balance
        

acc1 = Account(10000, 440580)
acc1.debit(500)
acc1.credit(2000)


