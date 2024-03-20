class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        total_sum=0
        right=0
        min_length=float('inf')
        left=0
        while right<len(nums):
             
             while total_sum<target  and right<len(nums):
                   total_sum+=nums[right]
                   right+=1
             while total_sum>=target and left<len(nums):
                   min_length=min(min_length,right-left)
                   total_sum-=nums[left]
                   left+=1
        if min_length==float('inf'):
                 return 0
        return min_length
             
                   