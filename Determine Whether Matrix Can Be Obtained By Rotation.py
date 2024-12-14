class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        #what are we going to do  to translate it into some thing which  is 90
        #here 
        for i in range(len(mat)*len(mat)):
            left,right=0,len(mat)-1
            while left<right:
                  top,bottom=left,right
                  for i in range(right-left):
                      topleft=mat[top][left+i]
                      mat[top][left+i]=mat[bottom-i][left]
                      mat[bottom-i][left]=mat[bottom][right-i]
                      mat[bottom][right-i]=mat[top+i][right]
                      mat[top+i][right]=topleft
                  left+=1
                  right-=1
            if mat==target:
               return True
        return False
