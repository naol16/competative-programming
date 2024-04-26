from collections import deque
 
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        mindequeue=deque()
        maxdequeue=deque()
        i=0
        answer=0
        for k in range(len(nums)):
           while maxdequeue and maxdequeue[-1]<nums[k]:
                 maxdequeue.pop()
           maxdequeue.append(nums[k])
           while mindequeue and mindequeue[-1]>nums[k]:
                 mindequeue.pop()
           mindequeue.append(nums[k])
           while maxdequeue[0]-mindequeue[0]>2:
                 if maxdequeue[0]==nums[i]:
                    maxdequeue.popleft()
                 if mindequeue[0]==nums[i]:
                    mindequeue.popleft()
                 i+=1
           answer+=k-i+1
        return answer
    
                