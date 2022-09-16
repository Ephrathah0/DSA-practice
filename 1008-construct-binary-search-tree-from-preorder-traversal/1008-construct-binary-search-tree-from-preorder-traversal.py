# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, root: Optional[TreeNode], n: int):
        if(n<root.val):
            if(root.left == None):
                root.left = TreeNode(n)
            else:
                self.buildTree(root.left, n)
        else:
            if(root.right == None):
                root.right = TreeNode(n)
            else:
                self.buildTree(root.right, n)
        return

            
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        r = TreeNode(preorder[0])
        for i in range(1, len(preorder)):
            self.buildTree(r, preorder[i])
        return r
        