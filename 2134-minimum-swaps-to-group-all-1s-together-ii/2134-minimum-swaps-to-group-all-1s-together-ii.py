
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        #first we  will find the window size 
        #the window size is the number one based on that we will find the minumum swap 
        total_number=nums.count(1)
        nums+=nums
        ones= nums[:total_number].count(1)
        minswap=total_number
        
        swap=0
        for i  in range(1,len(nums)-total_number+1):
            ones += nums[i + total_number - 1] - nums[i - 1]
            minswap=min(minswap,total_number-ones)
        print(ones)
        
        return minswap
