class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count=0
        total_product=1
        length=len(nums)
        left=0
        if k<=1:
           return 0
        
        for right in range(len(nums)):
        
            total_product*=nums[right]
            while left<length and total_product>=k:
                  total_product/=nums[left]
                  left+=1
            count+=right-left+1
        return count
            
            
            
            
        