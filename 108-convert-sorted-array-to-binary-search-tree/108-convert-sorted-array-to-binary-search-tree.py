# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        root = self.createtree(nums,0,len(nums)-1)
        return root
        
        
    def createtree(self,nums,left,right):
        if right == left:
            return TreeNode(nums[right])
        elif right > left:
            mid = (right + left +  1)// 2
            node = TreeNode(nums[mid])
            node.left = self.createtree(nums,left,mid - 1)
            node.right = self.createtree(nums,mid + 1, right)
            return node
        
        return 
        