class LRUCache:
    def __init__(self, capacity):
        self.dic = collections.OrderedDict()
        self.left = capacity
    def get(self, key):
        if key not in self.dic:
            return -1
        var = self.dic.pop(key) 
        self.dic[key] = var  
        return var
    def put(self, key, value):
        if key in self.dic:    
            self.dic.pop(key)
        else:
            if self.left > 0:
                self.left -= 1  
            else:  
                self.dic.popitem(last=False) 
        self.dic[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
