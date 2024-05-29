#print first n natural numbers

class One:



    def print_first_n_natural(self,n):
       if n>0:
           self.print_first_n_natural(n-1)
           print(n)



        
    def reverse_of_print(self,n):
        if n>0:
            print(n)
            return(self.reverse_of_print(n-1))
        

    def odd_natural(self,n):
        if n<=0 :
         return
        if  n%2!=0:
         print(n)
        self.odd_natural(n-1)


    def even_natural(self,n):
       if n<=0:
          return
       if n%2==0:
          print(n)
       self.even_natural(n-1)   


    def sum_first_n_natural(self,n):
       if n==1:
          return 1
       return n+self.sum_first_n_natural(n-1)
    

    def factorial(self,n):
       if n ==1:
          return 1
       return n*self.factorial(n-1)
    
    def sq_of_n_natural_numbers(self,n):
       if n<=0:
       
         return 0
       return n*n+self.sq_of_n_natural_numbers(n-1)
    

    def sum_even_natural_numbers(self,n):
       if n<=0:
          return 0
       if n%2==0:
         return n+self.sum_even_natural_numbers(n-1)
       else:
          return self.sum_even_natural_numbers(n-1)
       


    def sum_of_sq_of_even_nat_num(self,n):
       if n<=0:
          return 0
       if n%2==0:
          return n*n+self.sum_of_sq_of_even_nat_num(n-1)
       else:
          return self.sum_of_sq_of_even_nat_num(n-1)   
          
       
           
          
            
               

                  
        


obj=One()
obj.print_first_n_natural(10)  
print("-----------")
obj.reverse_of_print(10) 
print("-----------")     
obj.odd_natural(10)
print("-----------")
obj.even_natural(10)
print("-----------")
sum=obj.sum_first_n_natural(10)
print("sum-->",sum)
print("-----------")
print("fact-->",obj.factorial(10))
print("-----------")
res=obj.sq_of_n_natural_numbers(10)
print("sum of sq-->",res)
print("-----------")
sum_even=obj.sum_even_natural_numbers(10)
print("sum of even nat num-->",sum_even)

print("-----------")
print("-----------")
print("sum of sq of even==",obj.sum_of_sq_of_even_nat_num(10))