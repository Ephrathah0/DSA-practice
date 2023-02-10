class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        dic= collections.defaultdict(int)
        x, y = [], []
        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    x.append((i, j))
                if img2[i][j] == 1:
                    y.append((i, j))
        res = 0
        for a in x:
            for b in y:
                temp = (b[0]-a[0], b[1]-a[1])
                dic[temp] += 1
                res = max(res, dic[temp])
        return res
