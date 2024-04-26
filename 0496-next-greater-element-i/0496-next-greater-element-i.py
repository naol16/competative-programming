from collections import defaultdict
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dictionary=defaultdict(lambda:-1)
        stack=[]
        for  i in  range(len(nums2)):
             while stack and stack[-1]<nums2[i]:
                   num=stack.pop()
                   dictionary[num]=nums2[i]
             stack.append(nums2[i])
        return [dictionary[i] for i in nums1]
            
        
             
         