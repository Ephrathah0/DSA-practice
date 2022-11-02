class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        lst=[]
        for j in range(0, len(nums)+1):
            lst.append(j)
        for i in lst:
            if i not in nums:
                return i
           