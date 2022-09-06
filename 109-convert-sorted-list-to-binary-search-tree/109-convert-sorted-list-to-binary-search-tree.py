# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def BSTCreation(start,end):
            if start==end:
                return None
            slow = start
            fast = start.next
            while fast and fast.next and fast!=end and fast.next!=end:
                slow = slow.next
                fast = fast.next.next
            return TreeNode(slow.val,BSTCreation(start,slow),BSTCreation(slow.next,end))
        
        return BSTCreation(head,None)