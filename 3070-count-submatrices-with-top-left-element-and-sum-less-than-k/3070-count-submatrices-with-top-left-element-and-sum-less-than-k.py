class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        #we will use the concept of sliding window and 2d prefixsum concepts  togather
        #we will extend until the  right most part of 2d prefixsum is less than target value
        column=len(grid[0])
        row=len(grid)
        prefixsum=[[0]*(column+1) for i in range(row+1)]
        
        totalsum=0
        totalnum=0
        for i in range(0,row):
            for j in range(column):
                prefixsum[i+1][j+1]=(prefixsum[i][j+1]+prefixsum[i+1][j]-prefixsum[i][j]+grid[i][j])
        for i in range(1,len(prefixsum)):
            for j in range(1,len(prefixsum[0])):
                if prefixsum[i][j]<=k:
                    totalnum+=1
                else:
                     continue
        return totalnum


                
                