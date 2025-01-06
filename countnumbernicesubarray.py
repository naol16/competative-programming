class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # the  expanding  and shrinking
        left,middle = 0,0
        totalodd = 0
        totalnumber = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                totalodd += 1
        
            while k <totalodd :
                  value = nums[left]
                  if value % 2:
                      totalodd -= 1
                  left+=1
                  middle=left
            if totalodd == k:
               while not nums[middle]%2:
                     middle+=1
               totalnumber+=(middle-left)+1
               
        return totalnumber
