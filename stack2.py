class Stack(list):
    def is_empty(self):
        return len(self)==0
    
    def push(self,data):
        self.append(data)

    def pop(self):
        if not self.is_empty():
            super().pop()
        else:
             raise IndexError("empty stack")

    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise  IndexError("empty stack")

    def size(self):
        return len(self)       

#driver code
my_stk=Stack()
my_stk.push(10)
my_stk.push(20) 
my_stk.push(100)
my_stk.push(200)  
print("current stack=",my_stk)   
my_stk.peek()
my_stk.size()
my_stk.pop()
print("stack after pop",my_stk)