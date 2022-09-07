class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = 0
        odd = 1
        solution = [0]*len(nums)
        for num in nums:
            if num%2==0:
                solution[even] = num
                even += 2
            else:
                solution[odd] = num
                odd += 2
        return solution