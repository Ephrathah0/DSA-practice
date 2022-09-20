class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        maxHops = k+1
        
        graph = defaultdict(list)
        
        for (u,v,w) in flights:
            graph[u].append((v,w))
            
        
        cost = [float('inf')]*n 
        stops = [float('inf')]*n
        
        cost[src] = 0
        stops[src] = 0
        
        heap = [( stops[src], cost[src] ,src)]
        
        while heap:
            curStops, curCost, curNode = heappop(heap)
            
            for nbr,w in graph[curNode]:
                
                nextStops = curStops + 1
                nextCost = curCost + w
                

                if nextCost < cost[nbr] and nextStops <= k+1:
                    cost[nbr] = nextCost
                    stops[nbr] = nextStops
                    heappush(heap, ( nextStops, nextCost, nbr ))
            
    
        if cost[dst] != float('inf'):
            return cost[dst]
        else:
            return -1