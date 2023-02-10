class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        cnt = 0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target: 
                    cnt += 1
                if nums[j]+nums[i] == target: 
                    cnt += 1
        return cnt
