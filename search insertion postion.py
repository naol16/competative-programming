class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low,high=0,len(nums)-1
        while low<=high:
              middle=(low+high)//2
              if nums[middle]>target:
                 high=middle-1
              elif nums[middle]<target:
                   low=middle+1
              else:
                   return middle
        return low
