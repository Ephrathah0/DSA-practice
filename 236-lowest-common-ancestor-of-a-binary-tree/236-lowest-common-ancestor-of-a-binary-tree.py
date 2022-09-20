# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.lowest_ancestor = None
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def traverse_tree(curr_node):
            if not curr_node:
                return (False,False)
            left_tree = traverse_tree(curr_node.left)
            right_tree = traverse_tree(curr_node.right)
            p_found = left_tree[0] or right_tree[0] or curr_node == p
            q_found = left_tree[1] or right_tree[1] or curr_node == q
            
            if p_found and q_found and self.lowest_ancestor == None:
                self.lowest_ancestor = curr_node
            
            return (p_found, q_found)
        
        traverse_tree(root)
        return self.lowest_ancestor
        