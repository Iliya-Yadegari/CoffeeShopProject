import order as od



class Member():
    
    i = 0
    
    def __init__(self,balance):
        
        Member.i += 1
        self.i = 'mem' + str(Member.i)
        self.id = self.i
        self.balance = balance
        self.orders = []
        self.amountToPay = 0
    # def amountToPay(self):
    #     pay = od.o1.price * od.o1.quantity
    #     print(pay)
        
    def deposit(self,num):
        self.balance = self.balance + num
    
    def addOrder(self,order):
        self.orders.append(order)
        pay = order.price * order.quantity
        self.amountToPay += pay
    
    def orderToAdd(self,productM,priceM,quantityM):
        madeOrder = od.Order(productM,priceM,quantityM)
        self.orders.append(madeOrder)
        pay = madeOrder.price * madeOrder.quantity
        self.amountToPay += pay
        
