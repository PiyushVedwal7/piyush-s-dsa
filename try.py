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

    def print_list(self):
        temp = self.start
        while temp is not None:
            print("data --> " + str(temp.item))
            temp = temp.next




# Driver code
mylist = SLL()
mylist.insert_at_start(10)
mylist.insert_at_start(30)
mylist.insert_at_start(40)

mylist.print_list()

                            
                            
                            
                            
                            
                            

                            

                            


