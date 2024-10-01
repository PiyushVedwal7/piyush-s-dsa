class Recu:
    #def __init__():
    def fibo(n):
        if n<1:return -1
        if n==1 :return 0
        if n==2:return 1
        return Recu.fibo(n-1)+Recu.fibo(n-2)


 



if __name__ == "__main__":

    n=11
    
    for i in range(n):

       print(Recu.fibo(i))
           
        
