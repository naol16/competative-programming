class Solution:
    def __init__(self):
          self.s="0"
    def findKthBit(self, n: int, k: int) -> str:
        def reverse(a):
            return a[::-1]
        def invert(a):
            new1=""
            for i in a:
                if i=="0":
                   new1+="1"
                else:
                     new1+="0"
            return new1
        if n==0:
          
           return self.s[k-1]
        self.s=self.s+"1"+ reverse(invert(self.s))
        return self.findKthBit(n-1,k)
    
        
        
    
        