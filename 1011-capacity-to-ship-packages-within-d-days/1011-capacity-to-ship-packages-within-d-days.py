class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)-1
        right = sum(weights)
        while (right - left) > 1:
            cur_capacity = left + (right - left) // 2
            cumlative = 0
            cur_days = 1
            for w in weights:
                if cumlative + w <= cur_capacity:
                    cumlative += w
                else:
                    cumlative = w
                    cur_days += 1
            if cur_days <= days:
                # in this case you still can have smaller capacity.
                right = cur_capacity
            else:
                left = cur_capacity
        return right