class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        events = sorted([(t,i) for i,(s,t) in enumerate(intervals)])
        prev = float('-inf')
        res = 0
        for cur, i in events:
            if prev <= intervals[i][0]:
                res += 1
                prev = cur
        return len(intervals) - res