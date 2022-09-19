class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []
        
        for br in s:
            if br == '[':
                stack.append(br)
            else:
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(br)
        
        
        m, n = divmod(len(stack), 4)
        return m + 1 if n else m