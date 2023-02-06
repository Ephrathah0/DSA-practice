class Solution(object):
    def prefixCount(self, words, pref):
        ans=0
        for w in words:
            if pref==w[:len(pref)]:
                ans+=1
        return ans
