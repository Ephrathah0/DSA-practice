class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        def twoSum(nums,par,prev,low,high,tar):
            ans = []
            while low < high:
                if prev+par+nums[low]+nums[high] == tar:
                    ans.append([prev,par,nums[low],nums[high]])
                    while low < high and nums[low] == nums[low+1]:
                        low += 1
                    while high > low and nums[high] == nums[high-1]:
                        high -= 1 
                    low += 1
                    high -= 1
                elif prev+par+nums[low]+nums[high] > tar:
                    high -= 1
                else:
                    low += 1
            return ans
        def f(nums,tar):
            
            nums.sort()
            ans = []
            i = 0
            while i < len(nums):
                j = i+1
                while j < len(nums):
                    ans += twoSum(nums,nums[i],nums[j],j+1,len(nums)-1,tar)
                    while j < len(nums) - 1 and nums[j] == nums[j+1]:
                        j += 1
                    j += 1
                while i < len(nums) - 1 and nums[i] == nums[i+1]:
                    i += 1
                i += 1
            return ans
                
        return f(nums,target)