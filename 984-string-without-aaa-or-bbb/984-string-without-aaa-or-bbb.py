class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        n = 0
        res = ''
        while a and b:
            if n == -2 or (n != 2 and a >= b):
                res += 'a'
                a -= 1
                n = max(1, n + 1)
            else:
                res += 'b'
                b -= 1
                n = min(-1, n - 1)
        return res + (a * 'a') + (b * 'b')