class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        previous=[poured]
        for i in range(1,query_row+1):
            list1=[0]*(i+1)
            for k in range(i):
                firstvalue=previous[k]-1
                if firstvalue>0:
                    list1[k]+=0.5*firstvalue
                    list1[k+1]+=0.5*firstvalue
            previous=list1
        return min(1,previous[query_glass])
        
        
            
                  
                  
