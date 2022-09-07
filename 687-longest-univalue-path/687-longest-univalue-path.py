# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxx=0
    def univalue(self,root):
        if root==None:
            return [None,0]
        l=self.univalue(root.left)
        r=self.univalue(root.right)
        if root.val==l[0] and root.val==r[0]:
            self.maxx=max(self.maxx,l[1]+r[1]+1)
            return [root.val,1+max(l[1],r[1])]
        elif root.val==l[0] or root.val==r[0]:
            if root.val==l[0]:
                self.maxx=max(self.maxx,l[1]+1)
                return [root.val,1+l[1]]
            else:
                self.maxx=max(self.maxx,r[1]+1)
                return [root.val,1+r[1]]
        else:
            return [root.val,1]
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        z=self.univalue(root)
        if self.maxx==0:
            return 0
        return self.maxx-1