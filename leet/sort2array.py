class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #taking  3 pointers 
        p=m+n-1
        p1=m-1
        p2=n-1

        while p1>0 and p2>0:
            if nums1[p1]>nums2[p2]:
                nums1[p]=nums1[p1]
                p1=p1-1
            else:
                nums1[p]=nums2[p2]
                p2=p2-1
                p=p-1
        while p2>=0:
            nums1[p]=nums2[p2]
            p2=p2-1
            p=p-1            
        for i in range(len(nums1)-1):
            if nums1[i]>nums1[i+1]:
                temp=nums1[i]
                nums1[i]=nums1[i+1]
                nums1[i+1]=temp    