class Solution:
    def __init__(self):
          self.odd=4
          self.even=5
          self.total=1
          
        
    def countGoodNumbers(self, n: int) -> int:
        modulo=1000000007
        if n%2==1:
           even=(n//2)+1
           odd=n//2
           result=pow(5,even,modulo)*pow(4,odd,modulo)
           return result%modulo
        else:
            
             same=(n//2)
             result=pow(5,same,modulo)*pow(4,same,modulo)
             return result%modulo
        
            
             
        