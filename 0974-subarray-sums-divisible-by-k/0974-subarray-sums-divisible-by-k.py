class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dictionary={0:1}
        total_sum=0
        right=len(nums)
        count=0
        for i in range(right):
            total_sum+=nums[i]
            remainder=total_sum%k
            
            if remainder  in dictionary:
                 count+=dictionary[remainder]
                 dictionary[remainder]+=1
       
            if remainder not in dictionary:
               dictionary[remainder]=1
        return count
            