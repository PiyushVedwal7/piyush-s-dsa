#queue using linked list

class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class Queue:
    def __init__(self) -> None:
        self.front=None
        self.rear=None
        self.item_count=0

    def empty(self):
        return self.front==None
            

    def enqueue(self,data):
        n=Node(data)
        if self.empty():
            self.front=n
            
        else:
            self.rear.next=n
        self.rear=n
        self.item_count+=1

    def dequeue(self):
        if self.empty():
            raise IndexError("emoty")
        elif  self.front==self.rear:
            self.front=None
            self.rear=None
        else:
            self.front=self.front.next    
            self.item_count-=1


    def see_front(self):
        if self.empty():
            raise IndexError("emoty")
        else:

         return self.front.item

    def see_rear(self):
         if self.empty():
            raise IndexError("emoty")
         else:

          return self.rear.item

    def size(self):
        return self.item_count
    

    def print(self):
        temp=self.front
        for x in range(self.item_count):
            print(temp.item)

            temp=temp.next 


#driver code

my_q=Queue()
my_q.enqueue(10)
my_q.enqueue(20)
my_q.print()  
print("front",my_q.see_front())         
print("rear",my_q.see_rear())
print("size=",my_q.size())



              



        

        


        