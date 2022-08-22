class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:        
        stack = []
        
        for s, e in sorted(intervals):
            if stack and stack[-1][1] >= s:
                stack[-1] = [stack[-1][0], max(stack[-1][1], e)]
            else:
                stack.append([s,e])
                
        return stack