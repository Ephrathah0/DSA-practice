class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = [0] * len(prices)
        minimum = prices[0]
        
        for i in range(1, len(prices)):
            if prices[i] < minimum:
                minimum = prices[i]
            else:
                profits[i] = prices[i] - minimum
                
        return max(profits)
                    
     #   prices.sort()
      #  return(prices[-1]-prices[0])
     #  '''
      # for i in range(len(prices)):
       #     for j in range(len(prices+1)):                
        #        if prices[i]>prices[j]:
         #'''
    
            
            
            
        
        