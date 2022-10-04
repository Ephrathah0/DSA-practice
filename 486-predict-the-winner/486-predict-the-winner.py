class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        lookup = {}
        def fun(i,j, chance):
            if (i,j,chance) in lookup:
                return lookup[(i,j,chance)]
            
            if i > j:
                return 0
            
            if chance == 1:
                
                y =  max(nums[i] + fun(i+1, j, 2), nums[j] + fun(i, j-1, 2))
            else:
                
                y =  min(fun(i+1, j, 1), fun(i,j-1, 1))
                
            lookup[(i,j,chance)] = y
            return y
            
        max_p1_score = fun(0, len(nums)-1, 1)
        if max_p1_score >= sum(nums)/2:
            return True
        return False