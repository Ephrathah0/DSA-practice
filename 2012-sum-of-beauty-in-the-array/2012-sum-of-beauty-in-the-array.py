class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        cntNums, beauty = len(nums), 0
        prefix, suffix = [-math.inf for _ in range(cntNums)], [math.inf for _ in range(cntNums)]
        prefix[0], suffix[cntNums - 1] = nums[0], nums[cntNums - 1]
        for i in range(1, cntNums):
            prefix[i] = max(prefix[i - 1], nums[i])
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = min(suffix[i + 1], nums[i])
        for i in range(1, cntNums - 1):
            if prefix[i - 1] < nums[i] < suffix[i + 1]:
                beauty += 2
            elif nums[i - 1] < nums[i] < nums[i + 1]:
                beauty += 1
        return beauty