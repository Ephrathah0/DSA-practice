class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        queue = deque()
        if(root):
            queue.append(root)
        while(queue):
            node = queue.popleft()
            if(node.left and node.right):
                queue.append(node.left)
                queue.append(node.right)
                node.left.next = node.right
                if(node.next):
                    node.right.next = node.next.left
        return(root)