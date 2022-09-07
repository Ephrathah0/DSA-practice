class Solution:
    def romanToInt(self, number: str) -> int:
        m = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        return sum((m[f] if m[f] >= m[s] else -m[f] for f, s in itertools.pairwise(number)), m[number[-1]])