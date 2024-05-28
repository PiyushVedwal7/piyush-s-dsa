class PQ:
    def __init__(self):
        self.item=[]

    def push(self,data,prio):
        index=0
        while index<len(self.item) and self.item[index][1]<=prio:
            index+=1
        self.item.insert(index,(data,prio) )

    def is_empty(self):
        return len(self.item)==0

    def pop(self):
        if self.is_empty():
            raise IndexError("queue is empty")

        else:
          return  self.item.pop(0)[0]
        


    def size(self):
        return len(self.item)

#driver code

mypq=PQ()
mypq.push(10,1)
mypq.push(20,4)
size=mypq.size()
mypq.is_empty()
print("size=",size)

while not mypq.is_empty():

 print(mypq.pop())



