class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic={}
        
        for num in nums:
            if num in dic:
                dic[num]=dic[num]+1
            else:
                dic[num]=1
        res=0
        for i,j in dic.items():
            if dic[i] >= len(nums)/2:
                res=i
        return res
        