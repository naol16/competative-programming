class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count=0
        for i in range(len(nums)-1):
            right=i+1
            while  right<len(nums):
                   if nums[right]+nums[i]<target:
                      count+=1
                   right+=1
        return count
        