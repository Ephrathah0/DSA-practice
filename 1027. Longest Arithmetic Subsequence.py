class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        summ = [defaultdict(int) for _ in range(n)]
        res = 0
        for i in range(n):
            for j in range(i):
                d = nums[i] - nums[j]
                summ[i][d] = summ[j][d] + 1
                res = max(res, summ[i][d])
        return res + 1
