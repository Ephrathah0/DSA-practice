class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        val = 0
        x= len(s)-1
        while x>=0:
            if dic[s[x]] <= dic[s[x-1]] or x ==0:
                val+=dic[s[x]]
                x-=1
            else:
                val+= dic[s[x]] - dic[s[x-1]]
                x-=2
        return val
