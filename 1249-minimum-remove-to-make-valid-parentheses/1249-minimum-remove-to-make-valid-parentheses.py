class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        unclosed = 0
        num_closed = s.count(")")
        ans = []
        
        for char in s:
            if char == "(":
                if unclosed<num_closed:
                    ans+=char
                    unclosed+=1
            elif char == ")":
                if unclosed>0:
                    ans+=char
                    unclosed-=1
                num_closed-=1
            elif char != ")":
                ans+=char
        return "".join(ans)