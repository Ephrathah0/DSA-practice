class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        Sum=largestSum=nums[0]
        for i in range(1,len(nums)):
            Sum = max(nums[i],Sum+nums[i])
            largestSum= max (largestSum, Sum)
        return largestSum