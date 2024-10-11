class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n <= 1:
            return nums
    
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
    
        return merge(left, right)

    def merge(left, right):
        result = []
        k, l= 0, 0
        
        while k < len(left) and l < len(right):
            if left[k] <= right[l]:
                result.append(left[k])
                k += 1
            else:
                result.append(right[l])
                l+= 1
        
        result.extend(left[k:])
        result.extend(right[l:])
        
