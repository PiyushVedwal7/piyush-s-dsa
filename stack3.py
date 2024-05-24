class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class Stack:
    def __init__(self):
       self.start=None
       self.item_count=0

    def is_empty(self):
        return self.start==0
    
    def push(self,data):
        if self.is_empty():
            raise IndexError("empty stack")
        else:
            n=Node(data,self.start)
            self.start=n
            self.item_count+=1

    def pop(self):
        if self.is_empty():
            raise IndexError("empty stack")
        else:
            temp=self.start
            self.start=self.start.next
            popped=temp.item
            temp.next=None
        self.item_count-=1 
        return popped      


    def peek(self):
        if self.is_empty():
            raise IndexError("empty stack")   
        else:
            return self.start.item
        
    def size(self):
        return self.item_count
    
    


#driver code

my_stack=Stack()
my_stack.push(10)
my_stack.push(20)
my_stack.push(25)
peek=my_stack.peek()
size=my_stack.size()
popped=my_stack.pop()  

print("peek -> ",peek) 
print("size -> ",size)

print("popped elem ->",popped)



current = my_stack.start
print("Stack elements:")
while current:
    print(current.item, end=" -> ")
    current = current.next
    print("None")







    