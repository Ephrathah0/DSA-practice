class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)
        i = j = 0
        r = 0
        ans = y = x = 0
        while i < n:
            while r < n and minK <= nums[r] <= maxK:
                r += 1
            while (x == 0 or y == 0) and j < r:
                x += int(nums[j] == minK)
                y += int(nums[j] == maxK)
                j += 1
            if j == r and (x == 0 or y == 0):
                r += 1
                i = j = r
                x = y = 0 
            else:
                ans += r - j + 1
                x -= int(nums[i] == minK)
                y -= int(nums[i] == maxK)
                i += 1
        
        return ans
