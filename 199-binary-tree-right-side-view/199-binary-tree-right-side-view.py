class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q=collections.deque()
        ans=[]
        q.append((root))
        while q:
            l=len(q)
            for i in range(l):
                el=q.popleft()
                if i==0:
                    ans.append(el.val)
                if el.right:
                    q.append(el.right)
                if el.left:
                    q.append(el.left)
        return ans