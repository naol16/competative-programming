class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        answerarray=[]
        i=0
        j=0
        row=len(matrix)
        col=len(matrix[0])
        values=[(0,1),(1,0),(0,-1),(-1,0)]
        left,right=0,0
        index=0
        checker=[[True for i in range(len(matrix[0]))] for j in range(len(matrix))]
        while len(answerarray)<row*col:
              checker[left][right]=False
              answerarray.append(matrix[left][right])
              x1,x2=values[index]
              if  left+x1>=row or  right+x2>=col or checker[left+x1][right+x2]==False:
                  index=(index+1)%4
                  x1,x2=values[index]
              left=left+x1
              right=right+x2
        return answerarray
