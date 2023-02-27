class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        dic={}
        for i in logs:
            for j in range(i[0],i[1]):
                if j not in dic.keys():
                    dic[j]=0
                dic[j]+=1
        _max=0
        for i in dic.values():
            _max=max(_max,i)
        arr=[]
        for i in dic.keys():
            if dic[i]==_max:
                arr.append(i)
        arr= min(arr)
        return arr
            
