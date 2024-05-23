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
        else:
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
            return None
        else:
            temp = self.last.next
            while True:
                if temp.item == loc:
                    n = Node(data, temp.next)
                    temp.next = n
                    if temp == self.last:
                        self.last = n
                    break
                temp = temp.next
                if temp == self.last.next:
                    print(f"Location {loc} not found in the list.")
                    break

    def print_list(self):
        if self.is_empty():
            print("The list is empty.")
            return
        
        temp = self.last.next  # Start from the first node
        result = "list--> "
        while True:
            result += str(temp.item) + " "
            temp = temp.next
            if temp == self.last.next:  # Came back to the first node
                break
        print(result)

    def del_first(self):
        if self.is_empty():
            return None

        temp=self.last

        if temp.next==temp:
            temp=None
        elif temp.next!=temp:
            temp.next=temp.next.next


    def del_last(self):
        if self.is_empty():
            print("List is empty")
            return
        if self.last.next == self.last:
            self.last = None
        else:
                temp=self.last.next
                while temp.next!=self.last:
                    temp=temp.next

                    temp.next=self.last.next
                    self.last=temp



        


    def del_specific(self, data):
     if self.is_empty():
        print("List is empty")
        return

    # Case when there is only one element in the list
     if self.last.next == self.last:
        if self.last.item == data:
            self.last = None
        else:
            print(f"Element {data} not found in the list.")
        return

    # Case when there are multiple elements in the list
     temp = self.last.next
     prev = self.last

     while temp != self.last:
        if temp.item == data:
            prev.next = temp.next
            return
        prev = temp
        temp = temp.next

    # Check the last node separately
     if self.last.item == data:
        prev.next = self.last.next
        self.last = prev
     else:
        print(f"Element {data} not found in the list.")


# Driver code
my_cll = CLL()


my_cll.insert_start(10)


my_cll.insert_last(30)
my_cll.insert_after(15,10)
my_cll.insert_after(25,15)
my_cll.insert_after(30,25)
my_cll.insert_last(40)


my_cll.print_list()

print("searching")
find=my_cll.search(25)
if find:
    print("element exists")
else:
    print("not exist")

my_cll.del_first()
print("dele first")
my_cll.print_list()
my_cll.del_last()
my_cll.print_list()
print("last del")
my_cll.print_list()
#my_cll.del_specific(15)
print("after all del")
my_cll.print_list()