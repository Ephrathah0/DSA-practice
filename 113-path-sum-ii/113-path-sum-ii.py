# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
     def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def helper(root, targetSum, path):
            if root == None:
                return
            targetSum -= root.val
            path.append(root.val)
            if root.left == None and root.right == None:
                if targetSum == 0:
                    res.append(path[:])
                path.pop()  # backtrack 
                return
            helper(root.left, targetSum, path)
            helper(root.right, targetSum, path)
            path.pop()  # backtrack
        helper(root, targetSum, [])
        return res