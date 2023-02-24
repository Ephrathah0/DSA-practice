class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q = deque(tickets)
        time = 0
        while q[k]:
            if(q[0]==1):
                q.popleft()
                if(k==0):
                    return(time+1)
                else:
                    k -= 1
            else:
                q.append(q[0]-1)
                q.popleft()
                if(k==0):
                    k=len(q)-1
                else:
                    k-=1   
            time += 1       
        return time
                
            
            
                
            
