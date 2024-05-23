class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next

class DLL:
    def __init__(self,start=None) -> None:
        self.start=start
    def is_empty(self):
        if self.start is None:
            return True
        else:
            False
    def insert_at_start(self,data):
        n=Node(None,data,self.start)

        if  self.is_empty() is not True:
            self.start.prev=n
        else:
            self.start=n

    def insert_at_end(self,data):
        

        temp=self.start
        if temp is not None:
         while temp.next is not None:
            temp=temp.next
        n=Node(temp,data,None)
        temp.next=n
        n.prev=temp    



#need to correct this
    def random_insert(self,data,loc):
        temp=self.start
        if temp.item==loc:
            if temp.next==None:
                self.insert_at_end(data)
            else:
                n=Node(temp,data)    
                n.prev=temp
                temp.next=n
        else:
            temp=temp.next       



    def search(self,data):
        temp=self.start
        while temp is not None: 
            if temp.item==data:
                return True
            else:
                temp=temp.next


#issues
    def insert_after(self,temp,data):
        temp=self.start
        if temp is not None:
            n=Node(temp,data,temp.next)

            if temp.next is not None:
                temp.next.prev=n
                temp.next=n

    def delete_first(self):            
        temp=self.start
        if self.start is not None:
            self.start=temp.next
            if self.start.next is not None:
                self.start.next.prev=None
                temp.next=None


    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start=None
        else:
            temp=self.start
            while temp.next is not None:
              temp=temp.next
        temp.prev.next=None  



    def del_item(self,data):
        if self.start is None:
            pass
        else:
                temp=self.start
                while temp is not None:
                    if temp.item==data:
                        if temp.next is not None:
                            temp.next.prev=temp.prev
                        if temp.prev is not None:
                            temp.prev.next=temp.next
                        else:
                            self.start=temp.next
                        break
                    temp=temp.next    






    def print(self):
        temp=self.start
        while temp is not None:
            print("list="+str(temp.item))
            temp=temp.next
#driver
mydobly=DLL()

mydobly.insert_at_start(10)
mydobly.insert_at_end(50)
mydobly.insert_after(10,20)
mydobly.insert_after(20,30)
mydobly.insert_after(30,40)
print("initial list")
mydobly.print()
mydobly.del_item(50)
print("after del")
mydobly.print()
mydobly.delete_last()
print("list after del last elem")
mydobly.print()
