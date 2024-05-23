class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class CLL:
    def __init__(self, last=None) -> None:
        self.last = last

    def is_empty(self):
        return self.last is None

    def insert_start(self, data):
        n = Node(data)
        if self.is_empty():
            n.next = n
            self.last = n
        else:
            n.next = self.last.next
            self.last.next = n

    def insert_last(self, data):
        n = Node(data)
        if self.is_empty():
            n.next = n
            self.last = n
        else:
            n.next = self.last.next
            self.last.next = n
            self.last = n

    def search(self, data):
        if self.is_empty():
            return None
        temp = self.last.next
        while True:
            if temp.item == data:
                return temp
            temp = temp.next
            if temp == self.last.next:
                break
        return None

    def insert_after(self, data, loc):
        if self.is_empty():
            print("List is empty")
            return None
        temp = self.last.next
        while True:
            if temp.item == loc:
                n = Node(data, temp.next)
                temp.next = n
                if temp == self.last:
                    self.last = n
                return
            temp = temp.next
            if temp == self.last.next:
                break
        print(f"Location {loc} not found in the list.")

    def print_list(self):
        if self.is_empty():
            print("The list is empty.")
            return
        temp = self.last.next
        result = "list--> "
        while True:
            result += str(temp.item) + " "
            temp = temp.next
            if temp == self.last.next:
                break
        print(result)

    def del_first(self):
        if self.is_empty():
            print("List is empty")
            return
        temp = self.last.next
        if self.last.next == self.last:
            self.last = None
        else:
            self.last.next = temp.next

    def del_last(self):
        if self.is_empty():
            print("List is empty")
            return
        if self.last.next == self.last:
            self.last = None
        else:
            temp = self.last.next
            while temp.next != self.last:
                temp = temp.next
            temp.next = self.last.next
            self.last = temp

    def del_specific(self, data):
        if self.is_empty():
            print("List is empty")
            return
        if self.last.next == self.last and self.last.item == data:
            self.last = None
            return
        temp = self.last.next
        prev = self.last
        while temp != self.last:
            if temp.item == data:
                prev.next = temp.next
                return
            prev = temp
            temp = temp.next
        if self.last.item == data:
            prev.next = self.last.next
            self.last = prev

# Driver code
my_cll = CLL()

my_cll.insert_start(10)
my_cll.insert_last(30)
my_cll.insert_after(15, 10)
my_cll.insert_after(25, 15)
my_cll.insert_after(30, 25)
my_cll.insert_last(40)

print("Initial list:")
my_cll.print_list()

print("\nSearching for 25:")
find = my_cll.search(25)
if find:
    print("Element 25 exists")
else:
    print("Element 25 does not exist")

print("\nDeleting the first element:")
my_cll.del_first()
my_cll.print_list()

print("\nDeleting the last element:")
my_cll.del_last()
my_cll.print_list()

print("\nDeleting specific element 15:")
my_cll.del_specific(15)
my_cll.print_list()
