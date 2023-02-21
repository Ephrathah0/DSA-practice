class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        x = set()
        for i, j in edges:
            x.add(j) 
        res = []
        for a in range(n):
            if a not in x:
                res.append(a)
        return res
