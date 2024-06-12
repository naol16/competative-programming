class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        for i in edges:
            value1=i[0]
            value2=i[1]
            
            for j in range(1,len(edges)):
                if value2  in edges[j]:
                    return value2
                else:
                     return value1
                
                
        