class Solution:
    def sumZero(self, n: int) -> List[int]:
        output = [num for num in range(-n+1, n, 2)]
        return output
