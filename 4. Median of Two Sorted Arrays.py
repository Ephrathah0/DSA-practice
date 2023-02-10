class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        x=len(nums1)//2
        if len(nums1)%2!=0:
            s=(float(nums1[x]))
            return s
        elif len(nums1)%2==0:
            y=x
            z=x-1
        res=nums1[y]+nums1[z]
        med=(float(res)/float(2))
        return med
