# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.flattedList = []
        for i in range(len(nestedList)):
            nestedArray = self.flat(nestedList[i])
            self.flattedList.extend(nestedArray)
        print(self.flattedList)
        self.currentIndex = 0
    
    def flat(self, nestedInteger: NestedInteger) -> list:
        arr = []
        if nestedInteger.isInteger():
            arr.append(nestedInteger.getInteger())
        else:
            nestedIntegerList = nestedInteger.getList()
            for nestedInteger in nestedIntegerList:
                temp = self.flat(nestedInteger)
                arr.extend(temp)
        return arr
    
    def next(self) -> int:
        if self.currentIndex > len(self.flattedList) - 1:
            return self.flattedList[self.currentIndex]
        else:
            res = self.flattedList[self.currentIndex]
            self.currentIndex += 1                
            return res
        
    
    def hasNext(self) -> bool:
        if self.currentIndex > len(self.flattedList) - 1:
            return False
        return True

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
