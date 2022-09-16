class Solution:
    def buildTree(self, preorder, inorder):
        def loop(preorder, inorder):
            if not inorder:
                return None, preorder
            current = TreeNode(preorder[0])
            current_ind = inorder.index(current.val)
            preorder.remove(preorder[0])
            if len(inorder) == 3:
                if current_ind == 2:
                    current.left = TreeNode(inorder[current_ind-1])
                    current.right = None
                elif current_ind == 1:
                    current.left = TreeNode(inorder[current_ind - 1])
                    current.right = TreeNode(inorder[current_ind + 1])
                else:
                    current.left = None
                    current.right = TreeNode(inorder[current_ind + 1])
            current.left, preorder = loop(preorder, inorder[:current_ind])
            current.right, preorder = loop(preorder, inorder[current_ind+1:])
            return current, preorder
        return loop(preorder, inorder)[0]