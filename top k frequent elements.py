from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary=Counter(nums)
        heap=[]
        answerlist=[]
        heapify(heap)
    
        for i,j in dictionary.items():
            heappush(heap,(j,i))
        while len(heap)>k:
              heappop(heap)
        for i,j in heap:
            answerlist.append(j)
        return answerlist
               
        
