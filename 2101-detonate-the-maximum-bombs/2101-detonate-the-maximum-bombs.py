class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        temp = 0
        visited = set()
        
        def dfs(index, x, y, r):
            nonlocal temp
            if (x, y, r) in visited:
                return 
            visited.add((index, x,y,r))
            temp += 1
            for i, (a, b ,c) in enumerate(bombs):
                if (i, a, b, c) not in visited:
                    if ((x - a) * (x - a) + (y - b) * (y - b) <= r * r):
                        dfs(i, a, b, c)
                        
            
        ans = 0
        for i in range(len(bombs)):
            dfs(i, bombs[i][0], bombs[i][1], bombs[i][2])
            ans = max(ans, temp)
            temp = 0
            visited = set()
        return ans         