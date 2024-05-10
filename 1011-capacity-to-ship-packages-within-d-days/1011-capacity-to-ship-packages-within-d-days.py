class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lowest=max(weights)
        highest=sum(weights)
        result=highest
        count=0
        def checker(num):
            ships,curr=1,num
            for k in weights:
                if curr-k<0:
                   ships+=1
                   curr=num
                curr-=k
            return ships<=days
                
    
        
        while lowest<=highest:
              middle=lowest+(highest-lowest)//2
              if checker(middle):
                 highest=middle-1
              else:
                   lowest=middle+1
        return lowest
               
                    
              
                    
                    
                    
              
              
            
            
        