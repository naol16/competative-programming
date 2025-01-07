class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        left=0
        target=sum(nums)-x
        longestsub=0
        totalsum=0
        if target<0:
           return -1
        elif target==0:
             return len(nums)
        for i in range (len(nums)):
            totalsum+=nums[i]
            while totalsum>target:
                  totalsum-=nums[left]
                  left+=1
            if totalsum==target:
               longestsub=max(longestsub,i-left+1) 
        if longestsub==0:
           return -1
        return len(nums)-longestsub


       
