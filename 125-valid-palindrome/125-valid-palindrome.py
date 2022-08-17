class Solution:
    def isPalindrome(self, s: str) -> bool:
        x=s.lower()
        y=''.join(filter(str.isalnum, x))
        return True if y==y[::-1] else False