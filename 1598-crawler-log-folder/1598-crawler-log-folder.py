class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        count=0
        
        for i  in range(len(logs)):
            if logs[i]!='../' and logs[i]!='./': 
               count=count+1
            elif logs[i]=='../':
                 if count>0:
                    count-=1
                 
                      
        return count
        


               
         