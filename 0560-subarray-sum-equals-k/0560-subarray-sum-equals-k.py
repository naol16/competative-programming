class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        totalsum=0
        dictionary={0:1}
        count=0
        right=len(nums)
        for i in range(right):
            totalsum+=nums[i]
            if totalsum-k in dictionary:
               count+=dictionary[totalsum-k]
            if totalsum in dictionary:
               dictionary[totalsum]+=1
            else:
                  dictionary[totalsum]=1
        return count
               
        