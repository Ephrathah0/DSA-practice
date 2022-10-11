class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def enough(m, n, x, a):
            cnt = 0
            for i in range(1, m + 1):
                cnt += min(x // i, n)
            return cnt >= a
        l, r = 0, m * n
        while l < r:
            mid = l + (r - l) // 2
            if enough(m, n, mid, k):
                r = mid
            else:
                l = mid + 1
        return l
        