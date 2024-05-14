class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def checker(array):
            lowest=0
            highest=len(array)-1
            while lowest<=highest:
                  middle=(highest+lowest)//2
                  if array[middle]<target:
                     lowest=middle+1
                  elif array[middle]==target:
                       return True
                  else:
                       highest=middle-1
        for  array in matrix:
             if checker(array):
                return True
        return  False
                