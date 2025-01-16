class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left=0
        count=0
        for i in nums:
            if  i!=val:
                nums[left]=i
                count+=1
                left+=1
        
        return count
