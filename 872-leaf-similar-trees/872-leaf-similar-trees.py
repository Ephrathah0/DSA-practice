# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # dfs to maintain the sequence of leaves from left tpo right
        def dfs(root,arr=[]):
            if root:
			#check if it is a leaf and if yes then append to result array else continue dfs
                if not root.left and not root.right:
                    arr.append(root.val)
                left=dfs(root.left,arr)
                right=dfs(root.right,arr)
            return arr
        return dfs(root1,[])==dfs(root2,[])