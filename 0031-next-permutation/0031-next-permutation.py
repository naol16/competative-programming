class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        right=len(nums)-1
        pick=-1
        
        
        for i in range(0,right+1):
            if nums[i]>nums[i-1]:
                pick=i
        if pick==-1:
           return nums.sort()
        new_index=pick
        for i in range(pick,right+1):
            if nums[pick-1]<nums[i] and nums[i]<nums[new_index]:
               new_index=i
        nums[pick-1],nums[new_index]=nums[new_index],nums[pick-1]
        for j in range(pick,right):
            for i in range(pick,right):
                if nums[i]>nums[i+1]:
                   nums[i],nums[i+1]=nums[i+1],nums[i]
        return nums
              
         
        
                
                
                
                
        
                  
               
            
            
            
        

     
         

       