class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        s = set()
        def rec(nums,per):
            if not nums and tuple(per) not in s:
                res.append(per[::])
                s.add(tuple(per[::]))
                return 
            for i in range(len(nums)):
                newNums = nums[:i]+nums[i+1:]
                per.append(nums[i])
                rec(newNums,per)
                per.pop()
                
        rec(nums,[])
        return res