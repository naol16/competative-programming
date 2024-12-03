class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        
        
        maximum,minmum=0,0
        for i in range(indexDifference,len(nums)):
            if nums[i-indexDifference]<nums[minmum]:
                minmum=i-indexDifference
            if nums[i-indexDifference]>nums[maximum]:
                maximum=i-indexDifference
            if abs(nums[i]-nums[minmum])>=valueDifference:
                return  [i,minmum]
            if abs(nums[i]-nums[maximum])>=valueDifference:
                return  [i,maximum]
        return [-1,-1]
            
