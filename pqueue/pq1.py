class Node:
    def __init__(self, item=None, prio=None, next=None):
        self.item = item
        self.prio = prio
        self.next = next

class Prio:
    def __init__(self):
        self.start = None
        self.item_count = 0

    def is_empty(self):
        return self.start is None

    def push(self, data, prio):
        new_node = Node(data, prio)

        # If the list is empty or the new node has higher priority (lower prio value) than the start node
        if self.start is None or self.start.prio > prio:
            new_node.next = self.start
            self.start = new_node
        else:
            # Traverse the list to find the correct position to insert
            temp = self.start
            while temp.next is not None and temp.next.prio <= prio:
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node

        self.item_count += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("queue is empty")

        # Remove the start node and return its data
        data = self.start.item
        self.start = self.start.next
        self.item_count -= 1
        return data

    def size(self):
        return self.item_count

# Driver code
mypq = Prio()
mypq.push(10, 1)
mypq.push(20, 2)
mypq.push(5, 0)
mypq.push(15, 1)

size = mypq.size()
print("size -->", size)  # Should print 4

while not mypq.is_empty():
    print("popped -->", mypq.pop())  # Should print elements based on priority
