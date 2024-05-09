class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        high=len(nums)-1
        low=0
    
        while low<=high:
              middle=low+(high-low)//2
              if target>nums[middle]:
                 low=middle+1
              elif  target<nums[middle]:
                    high=middle-1
              elif target==nums[middle]:
                   rightmost=middle
                   leftmost=middle
                   while rightmost<len(nums) and target==nums[rightmost]:
                         rightmost+=1
                   while target==nums[leftmost] and leftmost>=0:
                         leftmost-=1
                   right=rightmost-1
                   left=leftmost+1
                   return [left,right]
        return[-1,-1]
