class Solution:
    def maximumBags(self, a: List[int], b: List[int], c: int) -> int:        
        res = 0
        l = sorted(zip(a,b),key=lambda x : x[0]-x[1])
        for i,j in l:
            if i-j==0 or c-(i-j)>=0:
                c = c-(i-j)
                res += 1
        return res