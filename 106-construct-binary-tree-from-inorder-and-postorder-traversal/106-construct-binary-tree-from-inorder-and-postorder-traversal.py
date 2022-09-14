class Solution(object):
    def build(self, i, p, i_1, i_2, p_1, p_2):
    
        if i_1 > i_2:
            return None
        
        if i_1 == i_2:
            return TreeNode(p[p_1], None, None)

        count = 0
        
        while i[i_2-count] != p[p_2]:
            count += 1
            
        node = TreeNode()
        
        node.val = p[p_2]
        node.left = self.build(i, p, i_1, i_2 - count - 1, p_1, p_2 - count - 1)
        node.right = self.build(i, p, i_2 - count + 1, i_2, p_2 - count, p_2 - 1)
            
        return node
        
    def buildTree(self, inorder, postorder):
        return self.build(inorder, postorder, 0, len(inorder)-1, 0, len(postorder)-1)