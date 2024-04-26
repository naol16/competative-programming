from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_queue=deque()
        min_queue=deque()
        j=0
        maximum=0
        for k,num in enumerate(nums):
            
            while max_queue and max_queue[-1]<num:
                  max_queue.pop()
            max_queue.append(num)
            while min_queue and min_queue[-1]>num:
                   min_queue.pop()
            min_queue.append(num)
            while max_queue[0]-min_queue[0]>limit:
                  if max_queue[0]==nums[j]:
                     max_queue.popleft()
                  if min_queue[0]==nums[j]:
                     min_queue.popleft()
                  j+=1
            maximum=max(maximum,k-j+1)
        return maximum