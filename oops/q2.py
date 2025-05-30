class Account:
    def __init__(self, bal, acno):
        self.bal = bal
        self.acno = acno
    def debit(self, debited):
        self.bal -= debited
        print("Rs.", debited, "debited from ", self.acno, "Available balance is ", self.bal)

    def credit(self, credited):
        self.bal += credited
        print("Rs.", credited, "credited in ", self.acno, "Available balance is ", self.bal)

totalBal = int(input("Total ballance : "))
debbal = int(input("Please enter balance you want to debit : "))
crebal = int(input("Please enter balance you want to creadit : "))
s1 = Account(totalBal, 123456)
s1.debit(debbal)
s1.credit(crebal)