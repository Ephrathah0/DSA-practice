class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        res = 0
        for i in words:
            s = 0
            j = 0
            g = True
            while s<len(S) and j<len(i):
                count_word = 0
                count_S = 0
                while s<len(S) and S[s]==i[j]:
                    count_S+=1
                    s+=1
                if count_S==0:
                    g = False
                    break
                s-=1
                while j<len(i) and S[s]==i[j]:
                    count_word+=1
                    j+=1
                if count_word == 0:
                    g = False
                    break
                s+=1
                if count_word>count_S or (count_word!=count_S and count_S<3):
                    g = False
                    break
            if s==len(S) and j==len(i) and g:
                res+=1
        return res
