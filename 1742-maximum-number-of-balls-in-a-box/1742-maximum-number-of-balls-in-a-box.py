class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        box = defaultdict(int)
        for ball in range(lowLimit, highLimit+1):
            idx = 0
            while ball:
                idx += ball % 10
                ball //= 10
            box[idx] += 1
        return max(box.values())
        