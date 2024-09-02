class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        s=[]
        for x in nums1:
            s.append(x)
        for x in nums2:
            s.append(x)
        s.sort()
        n=len(s)
        if n%2==0:
            return(s[n//2-1]+s[n//2])/2
        else:
            return s[n//2]