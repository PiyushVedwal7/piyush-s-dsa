from singly import *

class Stack:
    def __init__(self):
      self.mylist=SLL()
      self.item_count=0

    def is_empty(self):
       if self.mylist is None:
          raise IndexError("stack is empty")


    def push(self,data):
       self.mylist.insert_at_end(data)
       self.item_count+=1

    def pop(self):
       if self.mylist is None:
          raise IndexError("empty list")
       else:
          pop=self.mylist.delete_last()
          self.item_count-=1
       return pop      
    
    def size(self):
       return self.item_count

    def peek(self):
       if self.is_empty() is not True:
          return self.mylist.peek_last()  

#driver code

my=Stack()
my.push(100)
my.push(200)
my.push(300)
my.push(400)
my.push(500)
size=my.size()

print("size of stack = ",(size))      


popp=my.pop()
print("popped =",popp)

size2=my.size()

print("size of stack = ",(size2))      

peeked=my.peek()
print("peek =",peeked)


          
               
