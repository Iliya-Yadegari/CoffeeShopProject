class Shop:
    def __init__(self):
        self.members = []
    
    def hasMember(self,memid):
        for member in self.members:
            if member.id == memid:
                return True
            
            
      
        return False
            
    def addMember(self,mem):
        self.members.append(mem)
    
    def checkOut(self, checkOutMem_id):
        
        for mem in self.members:
            
            if mem.id == checkOutMem_id:
                mem.balance -= mem.amountToPay
                mem.orders.clear()
                mem.amountToPay = 0