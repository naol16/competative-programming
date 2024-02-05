class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        b=s.lower()
        newstring=''.join(c for c in b if c.isalnum())
        return newstring==newstring[::-1]
        
