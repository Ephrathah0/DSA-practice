class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        def dfs(r, c, i):
            if i == len(word) - 1 :
                return True 
            original = board[r][c]
            board[r][c] = "#" 
            for dx, dy in [[-1,0], [1,0], [0,-1],[0,1]]:
                dr = r + dy
                dc = c + dx
                if 0 <= dr < row and 0 <= dc < col and board[dr][dc] == word[i + 1]:
                    if dfs(dr, dc, i + 1):
                        return True 
            board[r][c] = original 
                    
        for r in range(row):
            for c in range(col): 
                i = 0 
                if board[r][c] == word[0]:
                    if dfs(r, c, i):
                        return True 
        return False 