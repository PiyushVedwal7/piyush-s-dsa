class Recursion:
    def cansum(arr,target):
        
        if target==0:
            return True
        if target<0:
            return False
        for num in arr:
            remainder=target-num
            if( Recursion.cansum(arr,remainder)):
                return True
        
        return False    


if __name__ == '__main__':
    arr=[2,3,4,5]
    target=1
    print(Recursion.cansum(arr,target))
