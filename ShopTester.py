'''
Note: Do not modify this file!

Good Luck!
'''

import order as od # Note that this should also added in member module
import member as mem
import shop as sh

		
print("(1.1)-------------------------------")
o1 = od.Order("Americano", 4.7, 2)
print(o1.product)
print(o1.price)
print(o1.quantity)

################################################################################

# print("(1.2)-------------------------------")
# o2 = od.Order() # Be creative here since __init__ expects 3 argument, what can we do?
# print(o2.product)
# print(o2.price)
# print(o2.quantity)
# o2.product = 'Americano' 
# o2.price = 4.7
# o2.quantity = 2
# print(o1.product)
# print(o1.price)
# print(o1.quantity)

################################################################################

print("(2)-------------------------------")
alan = mem.Member(20.0) # a member with initial balance 20.0
print(alan.id)
print(alan.balance)
alanOrders = alan.orders
print("Alan's number of orders: " , len(alanOrders))
print("Alan needs to pay: " , alan.amountToPay)

# ##############################################################################	

print("(3)-------------------------------");
mark = mem.Member(0) # a member with initial balance 0.0
print(mark.id)
print(mark.balance)
markOrders = mark.orders
print("Mark's number of orders: " , len(markOrders))
markPay = mark.amountToPay
print("Mark needs to pay: " , markPay)
mark.deposit(40.0)
print(mark.balance)

# ##############################################################################	

print("(4)-------------------------------")
alan.addOrder(o1)
alanOrders = alan.orders
print("Alan's number of orders: " , len(alanOrders))
alanOrder1 = alanOrders[0]
print("Product of Alan's 1st order: " , alanOrder1.product)
print("Price of Alan's 1st order: " , alanOrder1.price);
print("Quantity of Alan's 1st order: " , alanOrder1.quantity)
print("Alan needs to pay: " , alan.amountToPay)

# ##############################################################################	
# 		
print("(5)-------------------------------")
alan.orderToAdd("Caffe Latte", 5.5, 1)
alanOrders = alan.orders
print("Alan's number of orders: " , len(alanOrders))
alanOrder1 = alanOrders[0]
print("Product of Alan's 1st order: " , alanOrder1.product)
print("Price of Alan's 1st order: " , alanOrder1.price)
print("Quantity of Alan's 1st order: " , alanOrder1.quantity)
alanOrder2 = alanOrders[1]
print("Product of Alan's 2nd order: " , alanOrder2.product)
print("Price of Alan's 2nd order: " , alanOrder2.price)
print("Quantity of Alan's 2nd order: " , alanOrder2.quantity)
print("Alan needs to pay: " , alan.amountToPay)

# ##############################################################################	

print("(6)-------------------------------")
hollys = sh.Shop()
members = hollys.members
print("Number of members: " , len(members))
print("Alan is a memebr: " , hollys.hasMember(alan.id))
print("Mark is a memebr: " , hollys.hasMember(mark.id))

# ##############################################################################	

print("(7)-------------------------------")
hollys.addMember(alan)
hollys.addMember(mark)
members = hollys.members
print("Number of members: " , len(members))
# print("Member 1's id: " , members[0].id)
# print("Member 2's id: " , members[1].id)
print("Alan is a memebr: " , hollys.hasMember(alan.id))
print("Mark is a memebr: " , hollys.hasMember(mark.id))
# 	
# ##############################################################################	
# 	
print("(8)-------------------------------")
# # charge an existing member: deduct their balance. 
# hollys.checkOut(alan.id)
# hollys.checkOut(mark.id)
print("Member with id \"3\" exists: " , hollys.hasMember("3"))
# charge a non-existing member: do nothing.
# hollys.checkOut("3")
print("Alan's new balance: " , alan.balance)
print("Mark's new balance: " , mark.balance)

# ##############################################################################	
# 		
# # After charging a member with their current orders, 
# # we also clear all those orders. 
print("(9)-------------------------------");
alanOrders = alan.orders
print("Alan's number of orders: " , len(alanOrders))
alanPay = alan.amountToPay
print("Alan needs to pay: " , alanPay)

