class TimeMap:
    def __init__(self):
        self.keyvalue = collections.defaultdict(list)
        self.keytime = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keyvalue[key].append(value)
        self.keytime[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        # idx = bisect.bisect(self.keytime[key], timestamp)
        # if idx == 0:
        #     return ''
        # return self.keyvalue[key][idx - 1]
        times = self.keytime[key]
        if not times:
            return ""
        left, right = 0, len(times)-1
        
        mid = (left+right)//2
        while left<=right:
            
            if times[mid] == timestamp:
                return self.keyvalue[key][mid]
            if times[mid] > timestamp:
                right = mid - 1
            else:
                left = mid + 1
            mid = (left+right)//2    
            
        return  self.keyvalue[key][mid] if self.keytime[key][mid] <= timestamp else ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)