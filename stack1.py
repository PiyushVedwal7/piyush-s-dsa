class Stack:
    def __init__(self) -> None:
        self.items=[]

    def is_Empty(self):
        return len(self.items)==0
    
    def push(self,data):

        self.items.append(data)

    def pop(self):
        if not self.is_Empty():
            return self.items.pop() 
        else:
            return IndexError("stack is empty")

    def peek(self):
        if not self.is_Empty():
            return self.items[-1]
        else:
         return   IndexError ("empty stack")
        
    def size(self):
        if not self.is_Empty():
            return len(self.items)
        else:
            return IndexError("empty stack")    
        

#driver code

my_stack=Stack()

my_stack.push(10)
my_stack.push(20)
my_stack.push(30)
size=str(my_stack.size())
print("size of stack="+size)
my_stack.peek()
popped=str(my_stack.pop())
print("popped item="+popped)

                
