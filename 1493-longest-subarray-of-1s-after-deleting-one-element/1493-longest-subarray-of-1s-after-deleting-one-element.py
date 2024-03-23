class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum_length=0
        count_of_zero=0
        left=0
        right=0
        for right in range(len(nums)):
            if nums[right]==0:
               count_of_zero+=1
            while count_of_zero>1:
                  if nums[left]==0:
                     count_of_zero-=1
                  left+=1
            maximum_length=max(maximum_length,right-left)
        return maximum_length
               
            
        