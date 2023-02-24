class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        dic = defaultdict(set)
        for i,j in logs:
            dic[i].add(j)    
        ans = [0] * k
        for i in dic:
            ans[len(dic[i]) - 1] += 1
        return ans
