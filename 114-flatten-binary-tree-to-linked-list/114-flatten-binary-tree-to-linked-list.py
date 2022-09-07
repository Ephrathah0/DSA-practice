class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return 
        self.process(root)
        return 
    
    def process(self,root):
        if not root:
            return None, None
        
        lefthead, lefttail = self.process(root.left)
        righthead, righttail = self.process(root.right)
        
        root.left = None
        
        if not lefthead and not righthead:
            root.right = lefthead
            return root, root
        elif lefthead and not righthead:
            root.right = lefthead
            return root, lefttail
        elif not lefthead and righthead:
            root.right = righthead
            return root, righttail
        else:
            root.right = lefthead
            lefttail.right = righthead
            return root, righttail