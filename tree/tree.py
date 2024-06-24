class Node:
    def __init__(self,item=None,left=None,right=None):
        self.item=item
        self.left=left
        self.right=right

class BST:
    def __init__(self):
       self.root=None     

    def insert(self,root,data):
      self.root=self.rinsert(self.root,data)


    def rinsert(self,root,data):
        if root is None:
            return Node(data)

        elif data<root.item:
            self.root=self.rinsert(root.left,data)

        elif data>root.item:
            self.root=self.rinsert(root.right,data)

        return root    
    

    def search(self,data):
        return self.rsearch(self.root,data)
    
    def rsearch(self,root,data):
        if root is None or root.item==data:
            return root
        
        elif data<root.item:
            return self.rsearch(root.left,data)
        
        elif data>root.item:
            return self.rsearch(root.right,data)
        
        else:
            return ("no root found")
        


    def inorder(self):
        result=[]

        self.rinorder(self.root,result)

    def rinorder(self,root,result):
        if root:
            self.rinorder(root.left,result)
            result.append(root.item)
            self.rinorder(root.right,result)




#preorder    root left right
#pistorder  left right root
                  

    def max_value(self,temp):
        curr=temp
        while curr.right is not None:
            curr=curr.right
        return curr.item


    def min_value(self,temp):
        curr=temp
        while curr.left is not  None:

            curr=curr.left

        return curr.item



    def delete(self,data):


        self.root=self.rdelete(self.root,data)

    def rdelete(self,root,data):

        if root is None:

            return root
        
        if data<root.item:
            root.left=self.rdelete(root.left,data)

        elif data>root.item:
            root.right=self.rdelete(root.right,data)

        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                root.item=self.min_value(root.right)
            return self.rdelete(root.right,root.item)    






#driver code

tree=BST()

tree.insert(100,10)
found1=tree.search(10)
found2=tree.search(20)
print(found1)
print(found2)

