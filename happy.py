class Solution:
    def isHappy(self, n: int) -> bool:
        visted=set()
        n=str(n)
        result=0
        while n not in visted :
              visted.add(n)
              result=0
              for i in n:
                  result+=int(i)*int(i)
              n=str(result)
              if int(n)==1:
                 return True
        return False
