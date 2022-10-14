class Solution:
    def average(self, salary: List[int]) -> float:
        x=max(salary)
        y=min(salary)
        n=len(salary)-2
        output=sum(salary)-x-y
        
        return output/n
        
        