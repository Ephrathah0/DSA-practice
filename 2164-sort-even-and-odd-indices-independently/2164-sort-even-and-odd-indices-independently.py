class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even = [nums[i] for i in range(0 , len(nums)) if i % 2 == 0]
        odd = [nums[i] for i in range(0 , len(nums)) if i % 2 != 0]
        even.sort()
        odd = sorted(odd , reverse = True)
        even_index = 0
        odd_index = 0
        for i in range(0 , len(nums)):
            if i % 2 == 0:
                nums[i] = even[even_index]
                even_index += 1
            else:
                nums[i] = odd[odd_index]
                odd_index += 1
        return nums