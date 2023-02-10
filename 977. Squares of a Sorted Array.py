class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sqnums=[]
        for i in range(len(nums)):
            a=abs(nums[i])
            sqnums.append(a**2)
        sqnums.sort()    
        return sqnums
        
