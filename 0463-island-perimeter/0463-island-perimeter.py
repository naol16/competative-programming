class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        count=0
        for i,k in enumerate(grid):
             
             for j,w in enumerate(k):
                 value=0
                 if w==1:
                    count+=4
                    if i>0 and grid[i-1][j]==1:
                        count-=2
                    if  j>0 and  grid[i][j-1]==1:
                          count-=2
                        
        return count
                    
        
        