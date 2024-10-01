class Recu:
    #def __init__():
    def move( rows,cols):

        if (rows<0 or cols< 0):
            return 0
        if rows==0 or cols==0:
            return 0
        if rows==1 or cols==1:
            return 1 


        return  Recu.move(rows,cols-1)+Recu.move(rows-1,cols)

        

      

 



if __name__ == "__main__":
    
    print(Recu.move(2,3))

   
           
        
