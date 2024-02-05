class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        newlist=[]
        a=0
        b=0
        for i in range(len(nums)):
            for  j in range(i+1,len(nums)):
                 if nums[i]>nums[j]:
                      a+=1
            for j in range(0,i):
                if nums[i]>nums[j]:
                   b+=1
            c=a+b
        
            newlist.append(c)
            a=0
            b=0
        return newlist
