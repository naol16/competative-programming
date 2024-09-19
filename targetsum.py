class Solution:
      
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo={}
        def backtrack(totalsum,start):
            if start==len(nums):
                if totalsum==target:
                    return 1
                else:
                     return 0
            if (totalsum,start) in memo:
                return memo[(totalsum,start)]
            memo[(totalsum,start)]=backtrack(totalsum+nums[start],start+1) + backtrack(totalsum-nums[start],start+1)
            return memo[(totalsum,start)]
        return backtrack(0,0)
           
                
        
