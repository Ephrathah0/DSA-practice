class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        num, ans = 0, 0
        
        for c in s:
            if c == '(':
                num += 1
            else:
                if num == 0:
                    ans += 1
                else:
                    num -= 1
        ans += num
        return ans