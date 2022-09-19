class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        cache = {}
        m,n = len(grid),len(grid[0])
        lRow,lCol = m-1,n-1

        def dfs(i,j,bal):
            if i in [-1,m] or j in [-1,n] or bal<0:
                return False
            if (i,j,bal) not in cache:
                updatedBal = bal+(1 if grid[i][j]=='(' else -1)
                if (i,j) == (lRow,lCol) and updatedBal==0:
                    return True
                valid = dfs(i+1,j,updatedBal) or dfs(i,j+1,updatedBal)
                cache[(i,j,bal)] = valid
            return cache[(i,j,bal)]

        return dfs(0,0,0)
        