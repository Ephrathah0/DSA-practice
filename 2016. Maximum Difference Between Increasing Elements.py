class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maxdiff = -1
        minelement = nums[0]
        for i in range(len(nums)):
            minelement = min(minelement, nums[i])
            if minelement < nums[i] :
                diff = nums[i] - minelement 
                maxdiff = max(maxdiff, diff)
        return maxdiff
