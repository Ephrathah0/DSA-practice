# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        res=[]
        def leaf(node,height,value):
            if not node: return
            if node.left is None and node.right is None:
                res.append([height,value,node.val])
            leaf(node.left,height+1,value-1)
            leaf(node.right,height+1,value+1)
        leaf(root,0,0)
        res=sorted(res,key=lambda x:(x[0],-x[1]),reverse=True)
        return res[0][-1]