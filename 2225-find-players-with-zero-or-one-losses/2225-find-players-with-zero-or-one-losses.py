class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner = {}
        loser = {}
        
        for i in matches:
            if i[0] in winner:
                winner[i[0]] += 1
            else:
                winner[i[0]] = 1
                
            if i[1] in loser:
                loser[i[1]] += 1
            else:
                loser[i[1]] = 1
        
        winner_list = []
        loser_list = []
        
        for i in loser:
            if loser[i] == 1:
                loser_list.append(i)
        
        for i in winner:
            if i not in loser:
                winner_list.append(i)
                
        winner_list.sort()
        loser_list.sort()
                
        return [winner_list , loser_list]