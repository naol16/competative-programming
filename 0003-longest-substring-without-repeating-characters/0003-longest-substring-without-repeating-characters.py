from collections import defaultdict
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        charset=set()
        maximum=0
        left=0
        for i in range(len(s)):
            while s[i] in charset:
                  charset.remove(s[left])
                  left+=1
            charset.add(s[i])
            maximum=max(maximum,i+1-left)
        return maximum
            
    
             