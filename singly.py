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

    def insert_at_end(self, data):
        n = Node(data)
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n
        else:
            self.start = n

    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None

    def insert_after(self, node, data):
        if node is not None:
            n = Node(data, node.next)
            node.next = n
        else:
            print("The given previous node must be in the LinkedList.")

    def print_list(self):
        temp = self.start
        result = "list--> "
        while temp is not None:
            result += str(temp.item) + " "
            temp = temp.next
        print(result)

    def delete_last(self):
        if self.is_empty():
            print("List is empty")
            return
        if self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None    


    def peek_last(self):
        if self.is_empty():
            raise IndexError("empty list")
        temp = self.start
        while temp.next is not None:
            temp = temp.next
        return temp.item        

# Driver code
