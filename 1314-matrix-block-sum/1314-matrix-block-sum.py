class Solution(object):
    def matrixBlockSum(self, mat, k):
        """
        :type mat: List[List[int]]          01
        :type k: int
        :rtype: List[List[int]]
        """
        c=0
        d=0
        row,column=len(mat),len(mat[0])
        prefixsum=[[0]*(column+1) for _ in range(row+1)]
        for i in range(row):
            for j in range(column):
                prefixsum[i+1][j+1]=mat[i][j]+prefixsum[i][j+1]+prefixsum[i+1][j]-prefixsum[i][j]
        for i in range(row):
            for j in range(column):
                c = max(0, i - k)
                d = min(row - 1, i + k)
                e = max(0, j - k)
                f = min(column - 1, j + k)

                sum1=prefixsum[d+1][f+1]- prefixsum[d+1][e] - prefixsum[c][f+1] + prefixsum[c][e]
                mat[i][j]=sum1
        return mat
                
        
                
        
        