class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        c=0
        ans=0
        for i in range(len(nums)):
            if(nums[i]==1):
                c+=1
                ans=max(ans,c)
            else:
                c=0
        return(ans)