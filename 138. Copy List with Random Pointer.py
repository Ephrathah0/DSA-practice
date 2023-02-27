class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        stack = []
        dic = {}
        p = head
        while p :
            stack.append(p)
            dic[p] = Node(p.val)
            p = p.next
        dic[None] = None
        while stack :
            p = stack.pop(0)
            q = dic[p]
            q.next = dic[p.next]
            q.random = dic[p.random]
        return dic[head]
