from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustnums=set()
        trustedby=defaultdict(int)
        for i,j in  trust:
            trustedby[j]+=1
            trustnums.add(i)
        for i in range(1,n+1):
            if i not in trustnums and trustedby[i]==n-1:
               return i
            
        return -1
            
        
    
            
        