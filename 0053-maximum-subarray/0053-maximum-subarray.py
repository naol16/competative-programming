class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum_sum=float('-inf')
        minmum_sum=0
        total_sum=0
        for i in range(len(nums)):
            total_sum+=nums[i]
            maximum_sum=max(maximum_sum,total_sum,total_sum-minmum_sum,nums[i])
            minmum_sum=min(total_sum,minmum_sum)
        return maximum_sum
        