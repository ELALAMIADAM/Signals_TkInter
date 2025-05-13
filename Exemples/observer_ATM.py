from observer import *

class ATM(Subject):
    def __init__(self,name,amount):
        Subject.__init__(self)
        self.name=name
        self.amount=amount
    def get_name(self) :
        return self.name
    def get_amount(self) :
        return self.amount
    def fill(self,amount):
        self.amount=self.amount+amount
        self.notify()                    # Observer.update() calls
    def distribute(self,amount):
        self.amount=self.amount-amount
        self.notify()                    # Observer.update() calls

class Amount(Observer):
    def __init__(self,name):
        self.name=name
    def update(self, subject):           # call by Model.notify()
        print(self.name, subject.name, subject.amount)

if __name__ == "__main__" :
    amount=100
    subject=ATM("ATM1",amount)
    observer=Amount("Observer 1")
    subject.attach(observer)
    observer=Amount("Observer 2")
    subject.attach(observer)
    print("distribution de billets")
    for i in range(1,amount//20) :
        subject.distribute(i*10)
    print("Remplissage du distributeur de billets")
    subject.fill(amount)
    subject.detach(observer)
    print("distribution de billets")
    for i in range(1,amount//20) :
        subject.distribute(i*10)


