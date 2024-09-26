class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        summation=[[0]*len(obstacleGrid[0])]*len(obstacleGrid)
        if obstacleGrid[0][0]==0:
            summation[0][0]=1
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j]==1:
                    summation[i][j]=0
                else:
                     if i-1>=0 and j-1>=0:
                        summation[i][j]=summation[i-1][j]+summation[i][j-1]
                     elif i-1<0 and j>0:
                          summation[i][j]=summation[i][j-1]
                     elif i-1>0 and j<0:
                          summation[i][j]=summation[i][j-1]
        return summation[-1][-1]
