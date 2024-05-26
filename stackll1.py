from singly import *

class Stack(SLL):
    def __init__(self, start=None):
        super().__init__(start)
        self.item_count=0


    def empty(self):
        return super().is_empty()    
    
    def push(self,data):
        self.insert_at_end(data)
        self.item_count+=1

    def pop(self):
        if not self.empty():
            
            self.delete_last() 
            self.item_count-=1
        else:
            raise IndexError("empty stack")  

    def peek(self):
       return self.peek_last() 

    def size(self):
        return self.item_count        

#driver code

mylist=Stack()
mylist.push(1)
mylist.push(2)
mylist.push(3)
mylist.push(4)
size=mylist.size()
print("size-->",size)
pk=mylist.peek()
print("peek elem-->",pk)
mylist.pop()
apop=mylist.size()
print("size after pop-->",apop)


