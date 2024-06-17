from collections import defaultdict
from typing import List
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        dictionary={i:set() for i in range(n)}
        
        maxvalue=0
        for i,j in roads:   
            dictionary[i].add(j)
            dictionary[j].add(i)
        for i in range(n):
            for j in range(i+1,n):
            
                if j  in dictionary[i] :
                    value=len(dictionary[i])+len(dictionary[j])-1
                else:
                     value=len(dictionary[i])+len(dictionary[j])
                maxvalue=max(maxvalue,value)
        return maxvalue
            
        
        