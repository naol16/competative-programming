class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        y=str(x)
        
        #    return True
        # else:
        #      return False  
        length1=len(y)-1
        for i in range (0, len(y)):
            if y[i]!=y[length1-i]:
               return False
        return True
