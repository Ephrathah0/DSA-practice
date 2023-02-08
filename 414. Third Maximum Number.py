class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums=set(nums)
        nums=list(nums)
        nums=sorted(nums)
        if len(nums)<3:
            return max(nums)
        return nums[-3]
      
