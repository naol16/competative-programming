class Solution:
    def coloredCells(self, n: int) -> int:
        #first the color was blue 
        dp=[0 for i in range(n+1)]
        for  i in range(len(dp)):
             if i==0:
                dp[i]=0
             elif i==1:
                  dp[i]=1
             else:
                  dp[i]=(i-1)*4
        answer=sum(dp)
        return answer
