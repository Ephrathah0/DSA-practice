class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        N = len(nums)
        q = collections.deque()
        res = math.inf
        psum = [0] * (N + 1)
        for i in range(1, N + 1):
            psum[i] = psum[i - 1] + nums[i - 1]
        
        for ptr , temp in enumerate(psum):
            
            while q and temp <= psum[q[-1]]:
                q.pop()
            
            while q and temp - psum[q[0]] >= k:
                res = min(res, ptr - q.popleft())
            
            
            q.append(ptr)
        
        return res if res != math.inf else -1