class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visited = set()
        res = 0
        for num in nums:
            cnt = 0
            while num not in visited:
                visited.add(num)
                num = nums[num]
                cnt += 1
            res = max(res, cnt)
        return res