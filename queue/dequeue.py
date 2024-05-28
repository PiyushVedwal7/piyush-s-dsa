class DQ:
    def __init__(self) -> None:
        self.item=[]

    def empty(self):
        return len(self.item)==0

    def insert_front(self,data):
        self.item.insert(0,data)

    def insert_rear(self,data):
        self.item.append(data)

    def del_front(self):
        if self.empty():
            raise IndexError("empty")
        else:
            self.item.pop(0)

    def del_rear(self,data):
         if self.empty():
            raise IndexError("empty")
         else:
            self.item.pop()

    def see_front(self):
        if self.empty():
            raise IndexError("empty")
        else:

         return self.item[0] 


    def see_rear(self):
        if self.empty():
            raise IndexError("empty")
        else:

         return self.item[-1]  


    def size(self):
        return len(self.item)    


#driver 

my_dq=DQ()
my_dq.insert_front(10)
my_dq.insert_rear(40)
my_dq.insert_front(5)
my_dq.size()
my_dq.see_front()
my_dq.see_rear()
my_dq.del_front()
my_dq.see_rear()



