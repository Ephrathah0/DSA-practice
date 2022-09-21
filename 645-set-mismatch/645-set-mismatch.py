class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        s, l = set(), len(nums)
        for i in nums:
            if i not in s:
                s.add(i)
            else:
                return [i, (l + 1) * l // 2 - (sum(nums) - i)]