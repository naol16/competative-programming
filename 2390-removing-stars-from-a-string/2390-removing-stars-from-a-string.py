class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        list1=[]
        
        for i in range(len(s)):
            if s[i]=='*':
                list1.pop()
            else:
                 list1.append(s[i])
        return ''.join(list1)
            
            
      
             
                   
        