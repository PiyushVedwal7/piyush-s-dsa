#dq using doubly ll

class Node:
    def __init__(self,item=None,next=None,prev=None):
        self.item=item
        self.next=None
        self.prev=prev

class DQ:
    def __init__(self) -> None:
        self.item_count=0
        self.rear=None
        self.front=None

    def empty(self):
        return self.item_count==0

    def insert_front(self,data):
        n=Node(data,self.front,None)

        if self.empty():
            self.rear=n
        else:
            self.front.prev=None
            self.front=n
            self.item_count+=1

    def del_front(self):
        if self.empty():
            raise IndexError("empty queue") 
        if self.rear==self.front:
            self.front=None
            self.rear=None
        else:
            self.rear=self.front.next
            self.rear.next.prev=None
        self.item_count-=1


    def get_front(self):
        if self.empty():
            raise IndexError("empty")
        else:
         return self.front.item   

    def get_rear(self):
        if self.empty(self):
            raise IndexError("empty")
        else:
            return self.rear.item

    def size(self):
       return self.item_count         
    
#driver code
mydq=DQ()
mydq.insert_front(10)
    




