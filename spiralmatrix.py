class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        answer=[[0 for i  in range(n)] for j in range(n)]
        direction=[(0,1),(1,0),(0,-1),(-1,0)]
        checker=[[True for i in range(n)] for j in range(n)]
        left,right=0,0
        value=1
        row=n
        col=n
        index=0
        while value<=n*n:
              checker[left][right]=False
              answer[left][right]=value
              x1,x2=direction[index]
              if left+x1>=row or right+x2>=col or checker[left+x1][right+x2]==False:
                 index=(index+1)%4
              x1,x2=direction[index]
              left=left+x1
              right=right+x2
              value+=1
        return answer
            
              
                  
                 
                 
