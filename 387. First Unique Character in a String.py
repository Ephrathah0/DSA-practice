class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic={}
        for i in s:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for j, i in enumerate(s) :
            if dic[i] == 1 :
                return j
        return -1            
