class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dic={}
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        mark = sorted(dic.items(), key=lambda x:x[1], reverse=True)
        #sortdict = dict(mark)
        #print(sortdict)
        lst=[]
        print(mark)
        
        for i in range(k):
            lst.append(mark[i][0])
                
        return lst    
        
                
        
        