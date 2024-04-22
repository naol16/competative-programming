class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """ 
        dict1 = {
           '(' : ')',
       '{':'}',
       '[':']' }
   
        stack=[]
        for i in s:
            if i in dict1.keys():
               stack.append(i)
            else:
                 if not stack:
                    return False
                 
                    
                 if dict1[stack[-1]] != i:
                     return False
                 
                    
                 else:
                      stack.pop() 
            
        if stack:
           return False
        else:
             return True

          
    
  