class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        dic={")":"(", "}":"{", "]":"["}
        for x in s:
            if x in dic.values():
                stack.append(x)
            elif stack and dic[x]==stack[-1]:
                stack.pop()
            else:
                return False
        return stack==[]  