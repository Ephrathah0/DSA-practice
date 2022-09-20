# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def dfs(self, node, direction, visited,  path):
            if node in visited :
                return 
                        
            visited.add(node)
            path.append(direction)
            
            if node == destValue and len(path) < self.minlen:
                self.result = path.copy() 
                self.minlen = len(path)
            
            for j in graph[node]:
                nn = j[0]
                dd = j[1]
                dfs(self, nn, dd, visited, path)
            
            path.pop()
                      
        
        graph = defaultdict(list)
        Q = [root]
        while len(Q) > 0:
            node = Q.pop(0)
            if node.left is not None:
                Q.append(node.left)
                graph[node.val] += [(node.left.val, 'L')]
                graph[node.left.val] += [(node.val, 'U')]
            if node.right is not None:
                Q.append(node.right)
                graph[node.val] += [(node.right.val, 'R')]
                graph[node.right.val] += [(node.val, 'U')]
            
        self.result = []
        self.minlen = inf
        for i in range(len(graph[startValue])):
            direc = graph[startValue][i][1]
            dfs(self, startValue, direc, set(), [])
            
        out = ''.join(self.result[1:])
        return out
    