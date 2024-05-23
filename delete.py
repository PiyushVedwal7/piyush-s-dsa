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
    def delete(self,data):
        if self.start is None:
            pass
        else:
            if self.start.item==data:
                self.start=self.start.next

                return 
            temp=self.start

            while temp.next is not None:
                if temp.next.item==data:
                    temp.next=temp.next.next
                    return 
                temp=temp.next

    def print_list(self):
        temp = self.start
        while temp is not None:
            print("data --> " + str(temp.item))
            temp = temp.next


#driver code

mylist=SLL()
mylist.insert_at_start(10)
mylist.insert_at_start(20)
mylist.insert_at_start(30)
mylist.insert_at_start(40)
mylist.insert_at_start(50)
mylist.insert_at_start(60)
mylist.insert_at_start(70)
mylist.insert_at_start(80)
mylist.insert_at_start(90)
mylist.insert_at_start(100)
print("before deelte")
mylist.print_list()
print("//////////////////////////////")
print("after delte")
mylist.delete(80)
mylist.print_list()
print("/////////////////////////////")
print("round 2")
mylist.delete(40)
mylist.print_list()




