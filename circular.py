
class Node:
    def __init__(self,item=None,next=None):
      self.item=item
      self.next=next
class CLL:
    def __init__(self,last=None) -> None:
        self.last=last

    def is_empty(self):
        if self.last is None:
            return True


    def insert_start(self,data):
     n=Node(data)
     if self.is_empty():
        n.next=n
        self.last=n
     else:
        n.next=self.last.next
        self.last.next=n



    def insert_last(self,data):
       n=Node(data)
       if self.is_empty():
          n.next=n
          self.last=n
       else:
          n.next=self.last.next
          self.last.next=n
          self.last=n 


    



    def search(self,data):
       if self.is_empty():
          return None
       else:
          temp=self.last.next
          while temp!=self.last:
             if temp.item==data:
                return temp
             temp=temp.next


    def insert_after(self,data,loc):
       n=Node(data)
       if self.is_empty():
          return None
       else:
          temp=self.last.next
          while temp.item!=loc:
             n.next=temp.next
             temp.next=n
          else:
             temp=temp.next
                      
             
def print_list(self):
        """
        Print all the elements in the circular linked list.
        """
        if self.is_empty():
            print("The list is empty.")
            return
        
        temp = self.last.next  # Start from the first node
        result = "list--> "
        while True:
            result += str(temp.data) + " "
            temp = temp.next
            if temp == self.last.next:  # Came back to the first node
                break
        print(result)



#driver code

my_cll=CLL()
my_cll.insert_start(10)
my_cll.insert_last(20)
my_cll.print_list()




            


