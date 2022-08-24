class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        li = []
        
        s = sorted(score)
        ss = sorted(score, reverse = True)
        for i in range(len(score)):
            if score[i]==s[-1]:
                li.append("Gold Medal")
            elif score[i]==s[-2]:
                li.append("Silver Medal")
            elif score[i]==s[-3]:
                li.append("Bronze Medal")
                
            elif score[i] in ss:
                li.append(str(ss.index(score[i])+1))
        
        return li