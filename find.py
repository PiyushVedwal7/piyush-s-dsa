class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class SLL:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        return self.start is None

    def insert_at_start(self, data):
        n = Node(data, self.start)
        self.start = n

    def find(self,data):
        temp=self.start

        while temp is not None:
            if temp.item==data:
                return temp

            
            temp=temp.next 

        else:
            return None

#driver code

mylist=SLL()
mylist.insert_at_start(10)
mylist.insert_at_start(20)
mylist.insert_at_start(30)
found=mylist.find(10)  


if(found):
    print("sucess {found.item}")
else:
    print("fail")