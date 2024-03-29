class RandomizedSet:

    def __init__(self):
        self.indices = dict() 
        self.RandomList = []
              
    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False
        
        self.RandomList.append(val)
        self.indices[val] = len(self.RandomList) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False
        
        idx = self.indices[val]
        self.indices[self.RandomList[-1]] = self.indices[val]
        self.RandomList[idx], self.RandomList[-1] = self.RandomList[-1],self.RandomList[idx] 
        del self.indices[val]
        self.RandomList.pop()
        return True
        
    def getRandom(self) -> int:
        return random.choice(self.RandomList)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()