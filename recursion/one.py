class One:
    def f1(self,n):
        if n==1:
            return 1
        else:
            
        
            s= n+self.f1(n-1)

            return s
obj=One()
res=obj.f1(5)   
print(res)     