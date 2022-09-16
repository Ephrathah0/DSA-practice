class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nodes = {}
        
        def findDepth(node):
            if not node:
                return 0
            
            nodes[node] = (
                findDepth(node.left), 
                findDepth(node.right)
            )
            
            return max(nodes[node]) + 1
        
        findDepth(root)
        
        current = root
        
        while nodes[current][0] != nodes[current][1]:
            if nodes[current][0] < nodes[current][1]:
                current = current.right
            else:
                current = current.left
                
        return current