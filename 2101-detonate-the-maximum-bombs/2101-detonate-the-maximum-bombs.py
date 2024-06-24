from collections import defaultdict
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        dictionary=defaultdict(list)
        maximumsum=0
        for i in range(0,len(bombs)):
            for j in range(i+1,len(bombs)):
                x,y,z=bombs[i]
                e,f,g=bombs[j]
                value=sqrt(pow((f-y),2)+pow((e-x),2))
                if value <=z:
                   dictionary[i].append(j)
                if value<=g:
                   dictionary[j].append(i)
        def  dfs(i,visit):
             if i in visit:
                return 0
             visit.add(i)
             for k in dictionary[i]:
                 dfs(k,visit)
             return len(visit)
                
        for  i in range(len(bombs)):
             maximumsum=max(maximumsum,dfs(i,set()))
             
        return maximumsum
            
             
                
        
            
            
        
        
        
        
        