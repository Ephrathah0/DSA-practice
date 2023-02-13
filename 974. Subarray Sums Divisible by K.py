class Solution:
    def subarraysDivByK(self, A, K):
        summ, ans = 0, 0
        D = [0] * K
        D[0] = 1
        for i in A:
            summ = (summ + i) % K
            ans += D[summ]
            D[summ] += 1
        return ans
