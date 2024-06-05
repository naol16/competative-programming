class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combination=[]
        current=[]
        def back(num):
            if len(current)==k:
               combination.append(current[:])
               return 
                
            for  i in range(num,n+1):
                 current.append(i)
                 back(i+1)
                 current.pop()
        back(1)
        return combination
        
            
                 
            
        
        
        