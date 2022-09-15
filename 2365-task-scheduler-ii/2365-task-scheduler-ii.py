class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        time, last = 1, {}
        
        for task in tasks:
            done = last.get(task, -sys.maxsize)
            time = max(time, done + space) + 1
            last[task] = time
        
        return time - 1