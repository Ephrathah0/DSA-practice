class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        tracked = {0:-1}        
        count = 0               
        max_subarray_length = 0         
        for idx, val in enumerate(nums):             
            if val:
                count+=1 # Increment count by 1 
            else:
                count-=1 # Increment count by -1
            if count in tracked:
                max_subarray_length = max(max_subarray_length, idx - tracked[count])
            else:
                tracked[count] = idx
        
        return max_subarray_length