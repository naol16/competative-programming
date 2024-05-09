class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low=0
        highest=len(nums)-1
        
        while low<=highest:
              middle=(low+highest)//2
              if nums[middle]<target:
                 low=middle+1
              elif nums[middle]==target:
                   return middle
              else:
                   highest=middle-1
        return -1
                    
                   
                
                