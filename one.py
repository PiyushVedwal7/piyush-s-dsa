class Node:
 def __init__(self,item=None,next=None):

    self.item=item
    self.next=next


class SLL:

    def __init__(self,start=None):

     self.start=start 


    def is_empty(self):
        
        return self.start==None
    
    def insert_at_start(self,data):

        n=Node(self,data)

        self.start=n


        def insert_at_end(self,data):

            n=Node(data)   

            if not self.is_empty():
             temp=self.start

        if temp.next is not None :

         temp=temp.next
 
         temp.next=n 

        else:

         self.start=n


    def search(self,data):

     temp=self.start

     while temp is not None:

      if temp.item==data:
    
    
       temp=temp.next

     return None 


def insert_after(self,temp,data):
    
    if temp is not None :
     n =Node(data,temp.next)
    temp.next=n 

    def print(self):

        temp=self.start 
        while temp is not None:
            print("data--> "+str(temp.item))

            temp=temp.next

            #drivr code

            mylist=SLL()
            mylist.insert_at_start(100)
            mylist.insert_at_start(200)
            mylist.print()

