class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        ans = 0
        for i in range(len(s)): 
            for j in range(len(t)):
                start_s, start_t = i, j
                count = 0
                while(start_s<len(s) and start_t<len(t)):
                    if s[start_s]!=t[start_t]: 
                        count+=1
                    if count==1: 
                        ans+=1
                    if count>=2: 
                        break
                    start_s+=1
                    start_t+=1
        return ans
        