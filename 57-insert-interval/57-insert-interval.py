class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals or newInterval[0] > intervals[-1][1]:  # handling edge cases
            intervals += [newInterval]
            return intervals
        i,length = 0,len(intervals)
        start,end = newInterval
        while i < length:  # iterating over all the intervals
            s,e = intervals[i]
            if end < s: 
                intervals.insert(i,newInterval)
                return intervals
            if start > e:
                i += 1
                continue
            break   # breaking the loop once there is an overlap
        intervals[i] = [min(s,start),max(e,end)] # modifying the interval which broke the loop
        end = intervals[i][1]
        i += 1
        index = i
        while i < length:
            s,e = intervals[index]
            if end < s:
                return intervals
            if end > e:
                del intervals[index]
            else:
                intervals[index-1][1] = e
                end = e
                del intervals[index]
            i += 1
        return intervals