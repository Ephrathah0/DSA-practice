class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        def sumToN(n):
            return n * (n + 1) // 2

        nums.sort()
        prev = res = 0

        for num in nums:
            x = max(0, min(k, num - prev - 1))
            res += sumToN(prev + x) - sumToN(prev)
            k -= x
            if k == 0:
                return res
            prev = num
        
        return res + sumToN(prev + k) - sumToN(prev)