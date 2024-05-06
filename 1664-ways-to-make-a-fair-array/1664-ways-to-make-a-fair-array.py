class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
       
        even_total, odd_total = sum(nums[::2]), sum(nums[1::2])
        even, odd, result = 0, 0, 0
        for i, num in enumerate(nums):
            if i % 2 == 0:
                even_total -= num
                result += (even + odd_total == odd + even_total)
                even += num
            else:
                odd_total -= num
                result += (even + odd_total== odd+ even_total)
                odd += num
        return result