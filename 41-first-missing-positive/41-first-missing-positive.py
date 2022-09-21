class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while 1 <= (num := nums[i]) <= len(nums) and num != nums[num - 1]:
                nums[i], nums[num - 1] = nums[num - 1], nums[i]

        for expected, actual in enumerate(nums, 1):
            if expected != actual:
                return expected
        return len(nums) + 1