class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        
        def dfs(i, j):
            if not (0<=i<n and 0<=j<m): return
            if grid[i][j] == 0: return
            grid[i][j] = 0
            
            dirs = [(1, 0), (-1, 0), (0, 1), (0,-1)]
            
            for dx, dy in dirs:
                dfs(i+dx, j+dy)
            return
        
        for i in range(n):
            if i == 0 or i == n-1: 
                jrange = range(m)
            else:
                jrange = [0, m-1]
                
            for j in jrange:
                if grid[i][j] == 1:
                    dfs(i, j)
        
        ans = sum(sum(grid[i]) for i in range(n))
        
        return ans