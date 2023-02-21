class Solution:
    def parseNumber(self, s, i, isNegative=False):
        num = 0
        while i < len(s) and s[i].isdigit():
            num = num*10 + int(s[i])
            i += 1
        if isNegative:
            num = -num
        return NestedInteger(num), i    
    def parseList(self, s, i):
        obj = NestedInteger()
        while i < len(s) and s[i] != ']':
            if s[i].isdigit():
                data, idx = self.parseNumber(s, i)
                obj.add(data)
            elif s[i] == '-':
                data, i = self.parseNumber(s, i+1, True)
                obj.add(data)
            elif s[i] == '[':
                data, i = self.parseList(s, i+1)
                obj.add(data)
            else:
                i += 1

        return obj, i+1
    
    def deserialize(self, s: str) -> NestedInteger:
        if s[0] != '[':
            if s[0] == '-':
                nestedInteger, _ = self.parseNumber(s, 1, True)
            else:
                nestedInteger, _ = self.parseNumber(s, 0)
        else:
            nestedInteger, _ = self.parseList(s, 1)        

        return nestedInteger
