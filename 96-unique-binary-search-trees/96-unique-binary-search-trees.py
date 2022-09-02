class Solution:
    def numTrees(self, n: int) -> int:
        return reduce(lambda res, i: res * 2 * (2 * i + 1) // (i + 2), range(n), 1)
        