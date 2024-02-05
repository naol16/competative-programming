class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        rows,columns=len(matrix),len(matrix[0])
        self.sum=[[0]*(columns+1) for i in range(rows+1)]
        for c in range(rows):
            for r in range(columns):
                self.sum[c+1][r+1]=(self.sum[c+1][r]+self.sum[c][r+1]-self.sum[c][r]+matrix[c][r])


    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.sum[row2+1][col2+1]-self.sum[row2+1][col1]-self.sum[row1][col2+1]+self.sum[row1][col1]
        
