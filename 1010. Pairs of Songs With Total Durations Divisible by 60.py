class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        summ = [0] * 60
        n = 0
        for i in time:
            n += summ[(-1) * (i % 60)]
            summ[i % 60] += 1
        return n
