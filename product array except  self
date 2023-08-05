class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        array=[1]*len(nums)
        prefix=1
        suffix=1
        for i in range(len(nums)):
            array[i]=prefix
            prefix*=nums[i]
        for j in range(len(nums)-1,-1,-1):
            array[j]*=suffix
            suffix*=nums[j]
        return array
        
