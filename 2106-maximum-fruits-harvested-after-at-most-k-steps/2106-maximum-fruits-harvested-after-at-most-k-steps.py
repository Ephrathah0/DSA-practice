class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        
        steps, cumsum = 0, fruits[0][1]
        max_sum = 0
        i,j = 0,0
        
        while j<len(fruits):
            
            pos = min(abs(startPos-fruits[i][0]), abs(startPos-fruits[j][0]))
                
            if pos+steps <= k:
                max_sum = max(max_sum, cumsum)
                steps+= (fruits[j+1][0] - fruits[j][0]) if j+1<len(fruits) else 0
                cumsum += fruits[j+1][1] if j+1<len(fruits) else 0 
                j+=1
            else:
                if i==j:
                    
                    i+=1
                    j+=1
                    cumsum = fruits[i][1] if j<len(fruits) else 0
                    continue
                
                steps-= fruits[i+1][0] - fruits[i][0]
                cumsum -= fruits[i][1]
                i+=1
        
        return max_sum