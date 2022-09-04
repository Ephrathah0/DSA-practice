# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = dict()
        if not root :
            return []
        q = [[root,1]]
        
        while q:
            poped,l = q.pop(0)
            if l in d:
                d[l].append(poped.val)
            else:
                d[l] = [poped.val]
                
            if poped.left:
                q.append([poped.left,l+1])
            if poped.right:
                q.append([poped.right,l+1])
                
        left = True
        res = []
        for i in d:
            if left:
                res.append(d[i])
                left = False
            else:
                res.append(d[i][::-1])
                left = True
        return res