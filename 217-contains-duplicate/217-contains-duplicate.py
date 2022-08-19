class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return False if len(set(nums))== len(nums) else True       
        
        
        '''
        if len(set(nums))<len(nums):
            return True
        else:
            return False
        '''