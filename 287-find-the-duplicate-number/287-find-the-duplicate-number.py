class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l = set()
        for x in nums:
            if x in l: return x
            l.add(x)