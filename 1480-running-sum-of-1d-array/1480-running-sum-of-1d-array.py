class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        new_sum=[0]*len(nums)
        totalsum=0
        for i in range(len(nums)):
            totalsum+=nums[i]
            new_sum[i]=totalsum
        return new_sum