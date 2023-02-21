# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        tailA = headA
        tailB = headB
        while tailA != tailB:
            if tailA:
                tailA = tailA.next
            elif not tailA:
                tailA = headB
            if tailB:
                tailB = tailB.next
            elif not tailB:
                tailB = headA
        return tailA
