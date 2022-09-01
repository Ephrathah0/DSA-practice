class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        @cache
        def trees(start, end):
            ln, nodes = end - start + 1, nums[start:end + 1]
            if ln < 1:
                return [None]
            if ln == 1:
                return [TreeNode(nodes[0])]
            
            bsts = []
            for i in range(ln):
                lefts = trees(start, start + i - 1)
                rights = trees(start + i + 1, end)
                for subtree1 in lefts:
                    for subtree2 in rights:
                        root_here = TreeNode(nodes[i], subtree1, subtree2)
                        bsts.append(root_here)
                
            return bsts
        
        nums = list(range(1, n+1))
        return trees(0, n-1)