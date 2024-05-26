class Queue:
    def __init__(self) -> None:
        self.item=[]
        self.front=None
        self.rear=None
    def is_empty(self):
        return len(self.item)==0    

    def enqueue(self,data):
        self.item.append(data)    

    def dequeue(self):
        if self.is_empty():
            raise IndexError("empty queue")
        else:
            self.item.pop(0)

    def see_front(self):
        if self.is_empty():
            raise IndexError("sempty stack")
        else:
            return self.item[0]

    def see_rear(self):
        if self.is_empty():
            raise IndexError("sempty stack")
        else:
            return self.item[:-1]   

    def see_size(self):
        return len(self.item) 
    
    def print(self):
        for x in range(len(self.item)):
            print(self.item[x])
#driver code

my_q=Queue()
my_q.enqueue(10)
my_q.enqueue(20)
my_q.enqueue(30)
my_q.enqueue(40)
my_q.see_size()
my_q.see_front()
my_q.see_rear()
my_q.dequeue()
my_q.print()
   

    