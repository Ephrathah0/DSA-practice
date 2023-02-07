class Solution:
    def findKthLargest(self, nums, k):
        nums.sort()
        print(nums)
        return nums[len(nums)-k]
