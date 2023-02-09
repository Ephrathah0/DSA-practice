class Solution:
    def maximumSwap(self, num: int) -> int:
        _num = num
        for i in range(len(str(num))):
            nums = list(str(num))
            for j in range(i+1, len(str(num))):
                nums[i], nums[j] = nums[j], nums[i]
                x = ''.join(nums)
                _num = max(_num, int(x))
                nums[i], nums[j] = nums[j], nums[i]
        return _num
