class Shop:
    def __init__(self):
        self.members = []
    
    def hasMember(self,memid):
        for i in self.members:
            if i == memid:
                return True
            elif i == None:
                return False
            else:
                return False
    def addMember(self,mem):
        self.members.append(mem.id)