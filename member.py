import order as od



class Member():
    
    
    
    def __init__(self,balance):
        
        self.i = 0
        self.i += 1
        self.id = self.i
        self.balance = balance
        self.orders = []
    def amountToPay(self):
        pay = od.o1.price * od.o1.quantity
        print(pay)
        
    def deposit(self,num):
        self.balance = self.balance + num
    
    def addOrder(self,order):
        self.orders.append(order)
    
    def orderToAdd(self,productM,priceM,quantityM):
        madeOrder = od.Order(productM,priceM,quantityM)
        
        self.orders.append(madeOrder)