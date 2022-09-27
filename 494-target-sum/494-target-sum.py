class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        memcache = {}

        def findTargetSumWaysHelper(start_idx, cur_sum):
            if start_idx == len(nums):
                return 1 if cur_sum == target else 0
            if (start_idx, cur_sum) in memcache:
                return memcache[(start_idx, cur_sum)]

            add_ways = findTargetSumWaysHelper(start_idx + 1, cur_sum + nums[start_idx])
            sub_ways = findTargetSumWaysHelper(start_idx + 1, cur_sum - nums[start_idx])
            memcache[(start_idx, cur_sum)] = add_ways + sub_ways
            return memcache[(start_idx, cur_sum)]

        return findTargetSumWaysHelper(0, 0)